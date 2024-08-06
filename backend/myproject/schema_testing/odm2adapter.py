from .models import Agriculturalparcel

class OdmAdapter:
    def __init__(self):
        #self.db = 'farm'
        #self.odm2 = OdmAdapter()
        pass

    def insert_parcel(self, p_farm_name, p_plot_name):
        # Insert a parcel into the database
        try:
            parcel = Agriculturalparcel(farm_name=p_farm_name, plot_name=p_plot_name)
            parcel.save()
            return True
        except Exception as e:
            print(e)
            return False