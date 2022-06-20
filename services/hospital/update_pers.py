import multiprocessing
from hospital.models import *
from okb2.models import UpdatePers as UP
from okb2.models import UpdatePersData
from hospital.models import Sluchay,Patient
from django import db
from dbfread import DBF
import os
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from  django.conf import settings
import multiprocessing
from itertools import zip_longest
from threading import Thread
class UpdatePers:
    def __init__(self,user):
        self.user = User.objects.get(id=user)
        self.user_group_name = 'hospital_exportfrom1c_%s' % self.user.id

    @staticmethod
    def func_chunk_itertools(lst):
        i_ = iter(lst)
        return list(zip_longest(i_, i_, i_, i_, i_, i_, i_, i_, i_, i_))


    def update(self):
        UpdatePersData.objects.filter(user=self.user).all().delete()
        up = UP.objects.values('id').filter(user=self.user).all()
        procs = []
        for f in up:
            file = UP.objects.get(id=f['id'])
            dir = '/'.join([settings.MEDIA_ROOT, str(file.file)])
            queue = multiprocessing.Queue()
            queue_list = []
            db.connections.close_all()
            proc = multiprocessing.Process(target=self.insert,args=(dir,))
            procs.append(proc)
            proc.start()
        for p in procs:
            p.join()

    def insert(self,file):
        for rec in DBF(file, char_decode_errors="ignore", encoding="cp866", lowernames=True):
            rec.update({'user': self.user})
            UpdatePersData.objects.create(**rec)

    def update_pers(self):
        pers_data = UpdatePersData.objects.values('id').filter(user=self.user)
        pers = [UpdatePersData.objects.get(id=p['id']) for p in pers_data]
        chunk = self.func_chunk_itertools(pers)
        threads = []
        for c in chunk:
            t = Thread(target=self.up_data, args=(c,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        else:
            async_to_sync(get_channel_layer().group_send)(self.user_group_name,
                                                          {'type': 'update_pers', 'text': 'update'})


    def up_data(self,pers):
        for p in pers:
            if hasattr(p,'nhistory_r'):
                try:
                    sl = Sluchay.objects.get(nib=p.nhistory_r.split(' ')[0], datv=p.data_usl)
                except Sluchay.DoesNotExist:
                    sl = None
                if sl:
                    pat = Patient.objects.get(id = sl.patient.values('id')[0]['id'])
                    try:
                        doctype = F011.objects.get(id_doc=int(p.doctype_re),dateend=None) if p.doctype_re != '' else None
                    except F011.DoesNotExist:
                        doctype = None
                    except F011.MultipleObjectsReturned:
                        doctype = None

                    pat.udl = doctype if doctype != None else pat.udl
                    pat.s_pasp = p.docser_ree if len(p.docser_ree) > 0 else pat.s_pasp
                    pat.n_pasp = p.docnum_ree if len(p.docnum_ree) > 0 else pat.n_pasp
                    pat.ss = p.snils_ree if len(p.snils_ree) > 0 else pat.ss
                    pat.fam =  p.fam if len(p.fam) > 0 else pat.fam
                    pat.im = p.im if len(p.im) > 0 else pat.im
                    pat.ot = p.ot if len(p.ot) > 0 else pat.ot
                    pat.datr = p.dr if len(p.dr) > 0 else pat.datr
                    try:
                        w = V005.objects.get(id_pol=int(p.w), dateend=None) if p.w != '' else None
                    except V005.DoesNotExist:
                        w = None
                    pat.pol = w if w != None else pat.pol
                    try:
                        ctkom = Skom.objects.get(smo=str(float(p.smo)), dateend=None) if p.smo != '' else None
                    except Skom.DoesNotExist:
                        ctkom = None
                    except Skom.MultipleObjectsReturned:
                        ctkom = None
                    sl.vds.ctkom = ctkom if ctkom != None else sl.vds.ctkom
                    try:
                        t_pol = F008.objects.get(id_tip=p.vpolis, dateend=None) if p.vpolis != '' else None
                    except F008.DoesNotExist:
                        t_pol = None
                    except F008.MultipleObjectsReturned:
                        t_pol = None
                    sl.vds.t_pol = t_pol if t_pol != None else sl.vds.t_pol
                    sl.vds.sctp = p.spolis if len(p.spolis) > 0 else sl.vds.sctp
                    sl.vds.nctp = p.npolis if len(p.npolis) > 0 else sl.vds.nctp
                    pat.novor = p.novor if len(p.novor) > 0 else pat.novor
                    sl.vds.save()
                    sl.save()
                    pat.save()
