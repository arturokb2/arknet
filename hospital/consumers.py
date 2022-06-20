import json
from channels.generic.websocket import AsyncWebsocketConsumer
class ReportsMixConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.user_group_name = 'hospital_reports_mix_%s' % self.user_id
        print(self.user_group_name,'websocket')
        await self.channel_layer.group_add(self.user_group_name,
                                           self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        pass

    # async def report_data(self,event):
    #     # new_data = event['text']
    #     await self.send(json.dumps(event))

    async def download(self,event):
        # new_data = event['text']
        await self.send(json.dumps(event))

class ReportsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.user_group_name = 'hospital_reports_%s' % self.user_id
        await self.channel_layer.group_add(self.user_group_name,
                                           self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        pass

    async def report_data(self,event):
        # new_data = event['text']
        await self.send(json.dumps(event))

    async def download(self,event):
        await self.send(json.dumps(event))


    async def report_group_data(self,event):
        await self.send(json.dumps(event))

    async def report_vault_otd(self,event):
        await self.send(json.dumps(event))

    async def download_vault_otd(self,event):
        await self.send(json.dumps(event))

    async def report_group_data_a_oth(self, event):
        await self.send(json.dumps(event))

    async def download_a_oth(self,event):
        await self.send(json.dumps(event))
    

    async def error_messages(self,event):
        await self.send(json.dumps(event))
        

    # async def report_group_data_annual(self,event):
    #     await self.send(json.dumps(event))
    #
    # async def download_data_annual(self,event):
    #     await self.send(json.dumps(event))


class AnnualReportsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.user_group_name = 'hospital_annual_reports_%s' % self.user_id
        await self.channel_layer.group_add(self.user_group_name,
                                           self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        pass

    async def report_data(self,event):
        new_data = event['text']
        await self.send(json.dumps(new_data))

    async def download(self, event):
        await self.send(json.dumps(event))


    async def report_group_data_annual(self,event):
        await self.send(json.dumps(event))

    async def download_data_annual(self,event):
        await self.send(json.dumps(event))

class ReferenceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.user_group_name = 'hospital_reference_%s' % self.user_id
        await self.channel_layer.group_add(self.user_group_name,
                                           self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        pass

    async def report_data(self,event):
        new_data = event['text']
        await self.send(json.dumps(new_data))

class ExportFrom1cConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.user_group_name = 'hospital_exportfrom1c_%s' % self.user_id
        await self.channel_layer.group_add(self.user_group_name,
                                           self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        pass

    async def report_data(self,event):
        await self.send(json.dumps(event))

    async def progress(self,event):
        await self.send(json.dumps(event))

    async def update_pers(self, event):
        await self.send(json.dumps(event))


class CreateReestr(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.user_group_name = 'hospital_createreestr_%s' % self.user_id
        await self.channel_layer.group_add(self.user_group_name,
                                           self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        pass

    async def report_data(self,event):
        await self.send(json.dumps(event))

    async def progress(self,event):
        await self.send(json.dumps(event))

    async def download(self, event):
        await self.send(json.dumps(event))

    async def download_reestr_prot(self,event):
        await self.send(json.dumps(event))



class Hospital(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']
        self.user_group_name = 'hospital_user_all'
        await self.channel_layer.group_add(self.user_group_name,
                                           self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        pass

    async def message(self,event):
        await self.send(json.dumps(event))