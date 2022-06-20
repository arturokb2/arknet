from hospital.models import Sluchay, Patient,Vb_s
from okb2.models import MyUser

class Search_history:
    def __init__(self, history, user):
        self.history = str(history).strip()
        self.user = MyUser.objects.get(user=user)

    def get_history(self):
        data = dict()
        history = list()
        # sl = Sluchay.objects.values('id').filter(nib__icontains=self.history, statistics_type=self.user.statistics_type)[:10]
        sl = Sluchay.objects.values('id').filter(nib__icontains=self.history)[:10]
        for s in sl:
            data.clear()
            patient = Patient.objects.get(sluchay=s['id'])
            # sluch = Sluchay.objects.get(id=s['id'])
            # vb_s = Vb_s.objects.get(id=sluch.vb_s.values('id')[0]['id']) if (sluch.vb_s.count() > 0) else None
            # if (sluch.statistics_type == self.user.statistics_type) or (vb_s != None and vb_s.potd != None and vb_s.potd.tipe ==  self.user.ws.kod):
            # if (sluch.statistics_type == self.user.statistics_type):
            data['id'] = s['id']
            data['nhistory'] = patient.sluchay.values('nib')[0]['nib']
            data['fam'] = patient.fam
            data['im'] = patient.im
            data['ot'] = patient.ot
            data['dr'] = patient.datr
            data['date_z_1'] = patient.sluchay.values('datp')[0]['datp']
            history.append(data.copy())
        return history