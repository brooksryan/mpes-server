from django.apps import AppConfig


class TicksapiConfig(AppConfig):
    name = 'ticksApi'
    
    def ready(self):
        
        import ticksApi.modelSignals
