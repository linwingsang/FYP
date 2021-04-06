from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_appbuilder.baseviews import expose, BaseView
from . import appbuilder, db
from .models import test,Deliveryman,Income,Vip,Live,Log,Comments,Profiles,Favorite,Ranking,Orderheaders,Orderslines,Tip,Orderhistorys,Refunds,Orderspeca
from .models import Cartheaders,Cartlines,Specialneeds,Restaurant,Foodtype,Foodoption,Notices,Grade,Promotion,Events,Othervariety,Cuisine
from .models import Payments, Paymethods, Coupons, Commerces, Monthreport, Yearreport
"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""User"""

def vip_query():
    return db.session.query(Vip)
    
class LiveView(ModelView):
      datamodel = SQLAInterface(Live)
      label_columns = {'vip.name':'username'}
      list_columns = ['id','vip.name','address','note']
     
      edit_form_extra_fields = {'vip':  QuerySelectField("Vip",
                                query_factory=vip_query,
                                widget=Select2Widget(extra_classes="readonly"))}    

class CommentsView(ModelView):
      datamodel = SQLAInterface(Comments)
      label_columns = {'vip.name':'username'}
      list_columns = ['id','vip.name','text']
     
      edit_form_extra_fields = {'vip':  QuerySelectField("Vip",
                                query_factory=vip_query,
                                widget=Select2Widget(extra_classes="readonly"))}    

class FavoriteView(ModelView):
      datamodel = SQLAInterface(Favorite)
      label_columns = {'vip.name':'username', 'restaurant_name':'restaurant'}
      list_columns = ['id','vip.name','restaurant_name']
     
      edit_form_extra_fields = {'vip':  QuerySelectField("Vip",
                                query_factory=vip_query,
                                widget=Select2Widget(extra_classes="readonly"))} 

class ProfilesView(ModelView):
      datamodel = SQLAInterface(Profiles)
      label_columns = {'vip.name':'username'}
      list_columns = ['id','vip.name','tel_no','email']
     
      edit_form_extra_fields = {'vip':  QuerySelectField("Vip",
                                query_factory=vip_query,
                                widget=Select2Widget(extra_classes="readonly"))} 

class LogView(ModelView):
      datamodel = SQLAInterface(Log)
      label_columns = {'vip.name':'username'}
      list_columns = ['id','vip.name','date_in']
     
      edit_form_extra_fields = {'vip':  QuerySelectField("Vip",
                                query_factory=vip_query,
                                widget=Select2Widget(extra_classes="readonly"))} 


class VipView(ModelView):
     datamodel = SQLAInterface(Vip)
     list_columns = ['id','name','password','role']
     related_views = [LiveView, CommentsView, FavoriteView, ProfilesView, LogView]


"""restaurant"""
def restaurant_query():
    return db.session.query(Restaurant)
    
class FoodtypeView(ModelView):
      datamodel = SQLAInterface(Foodtype)
      label_columns = {'restaurant.name':'Restaurant','item_name':'item name','price':'price ($HK)'}
      list_columns = ['id','restaurant.name','item_name','description','price']
     
      edit_form_extra_fields = {'restaurant':  QuerySelectField("Restaurant",
                                query_factory=restaurant_query,
                                widget=Select2Widget(extra_classes="readonly"))} 

class FoodoptionView(ModelView):
      datamodel = SQLAInterface(Foodoption)
      label_columns = {'restaurant.name':'Restaurant','option_name':'option name'}
      list_columns = ['id','restaurant.name','option_name']
     
      edit_form_extra_fields = {'restaurant':  QuerySelectField("Restaurant",
                                query_factory=restaurant_query,
                                widget=Select2Widget(extra_classes="readonly"))} 

class NoticesView(ModelView):
      datamodel = SQLAInterface(Notices)
      label_columns = {'restaurant.name':'Restaurant'}
      list_columns = ['id','restaurant.name','notice']
     
      edit_form_extra_fields = {'restaurant':  QuerySelectField("Restaurant",
                                query_factory=restaurant_query,
                                widget=Select2Widget(extra_classes="readonly"))} 

class GradeView(ModelView):
      datamodel = SQLAInterface(Grade)
      label_columns = {'restaurant.name':'Restaurant'}
      list_columns = ['id','restaurant.name','grade']
     
      edit_form_extra_fields = {'restaurant':  QuerySelectField("Restaurant",
                                query_factory=restaurant_query,
                                widget=Select2Widget(extra_classes="readonly"))} 

class PromotionView(ModelView):
      datamodel = SQLAInterface(Promotion)
      label_columns = {'restaurant.name':'Restaurant','discount':'Discount (%)'}
      list_columns = ['id','restaurant.name','discount']
     
      edit_form_extra_fields = {'restaurant':  QuerySelectField("Restaurant",
                                query_factory=restaurant_query,
                                widget=Select2Widget(extra_classes="readonly"))} 

class EventsView(ModelView):
      datamodel = SQLAInterface(Events)
      label_columns = {'restaurant.name':'Restaurant','event_name':'event name','start_date':'Start date','end_date':'End date'}
      list_columns = ['id','restaurant.name','event_name','start_date','end_date']
     
      edit_form_extra_fields = {'restaurant':  QuerySelectField("Restaurant",
                                query_factory=restaurant_query,
                                widget=Select2Widget(extra_classes="readonly"))} 
                                
class OthervarietyView(ModelView):
      datamodel = SQLAInterface(Othervariety)
      label_columns = {'restaurant.name':'Restaurant','item_name':'item name'}
      list_columns = ['id','restaurant.name','item_name']
     
      edit_form_extra_fields = {'restaurant':  QuerySelectField("Restaurant",
                                query_factory=restaurant_query,
                                widget=Select2Widget(extra_classes="readonly"))}     
                                
class CuisineView(ModelView):
      datamodel = SQLAInterface(Cuisine)
      label_columns = {'restaurant.name':'Restaurant','item_name':'item name'}
      list_columns = ['id','restaurant.name','item_name']
     
      edit_form_extra_fields = {'restaurant':  QuerySelectField("Restaurant",
                                query_factory=restaurant_query,
                                widget=Select2Widget(extra_classes="readonly"))}                                 


class RestaurantView(ModelView):
     datamodel = SQLAInterface(Restaurant)
     label_columns = {'tel_number':'Tel Number','collection_point':'Collect Point'}
     list_columns = ['id','name','location','address','tel_number','category','collection_point']
     related_views = [FoodtypeView,FoodoptionView,NoticesView,GradeView,EventsView,PromotionView, OthervarietyView,CuisineView]    



class RankingView(ModelView):
     datamodel = SQLAInterface(Ranking)
     label_columns = {'Restaurant_name':'Restaurant'}
     list_columns = ['rank','Restaurant_name','total_order']

"""basket"""
def cartheaders_query():
    return db.session.query(Cartheaders)

class CartlinesView(ModelView):
    datamodel = SQLAInterface(Cartlines)
    label_columns = {'price':'price ($HK)','cartheaders.id':'Cart Header ID'}
    list_columns = ['id','cartheaders.id', 'item_name','description','price']
    edit_form_extra_fields = {'cartheaders':  QuerySelectField('Cartheaders',
                                query_factory=cartheaders_query,
                                widget=Select2Widget(extra_classes="readonly"))}

class SpecialneedsView(ModelView):
    datamodel = SQLAInterface(Specialneeds)
    label_columns = {'cartheaders.id':'Cart Header ID','sweetlevel':'sweetlevel (none/low/heavy)','icelevel':'icelevel (none/low/heavy)','ricelevel':'ricelevel (low/heavy)','drinkingstraw':'drinkingstraw (none)'}
    list_columns = ['id','cartheaders.id','sweetlevel','icelevel','ricelevel','drinkingstraw']
    edit_form_extra_fields = {'cartheaders':  QuerySelectField('Cartheaders',
                                query_factory=cartheaders_query,
                                widget=Select2Widget(extra_classes="readonly"))} 
    
class CartheadersView(ModelView):
    datamodel = SQLAInterface(Cartheaders)
    label_columns = {'Collectlocation':'Collect location'}
    list_columns = ['id','username','Collectlocation','Cart_date']
  
    related_views = [CartlinesView, SpecialneedsView]


"""order"""
   
def orderheaders_query():
    return db.session.query(Orderheaders)
    
def payments_query():
    return db.session.query(Payments)    
    
class OrderslinesView(ModelView):
    datamodel = SQLAInterface(Orderslines)
    list_columns = ['id','orderheaders.id','restaurant.name', 'item_name','description','price']
    edit_form_extra_fields = {'orderheaders':  QuerySelectField('Orderheaders',
                                query_factory=orderheaders_query,
                                widget=Select2Widget(extra_classes="readonly"))}
    edit_form_extra_fields = {'restaurant':  QuerySelectField("Restaurant",
                                query_factory=restaurant_query,
                                widget=Select2Widget(extra_classes="readonly"))}   
        
class TipView(ModelView):
    datamodel = SQLAInterface(Tip)
    label_columns = {'tip':'Tips ($HK)'}
    list_columns = ['id','orderheaders.id', 'tip','tip_comment']
    edit_form_extra_fields = {'orderheaders':  QuerySelectField('Orderheaders',
                                query_factory=orderheaders_query,
                                widget=Select2Widget(extra_classes="readonly"))}

class OrderhistorysView(ModelView):
    datamodel = SQLAInterface(Orderhistorys)
    list_columns = ['id','orderheaders.id']
    edit_form_extra_fields = {'orderheaders':  QuerySelectField('Orderheaders',
                                query_factory=orderheaders_query,
                                widget=Select2Widget(extra_classes="readonly"))}
                
class RefundsView(ModelView):
    datamodel = SQLAInterface(Refunds)
    label_columns = {'orderheaders.Username':'Username','orderheaders.id':'Order Number'}
    list_columns = ['id','orderheaders.id','orderheaders.Username','amount','status','refund_date']
    edit_form_extra_fields = {'orderheaders':  QuerySelectField('Orderheaders',
                                query_factory=orderheaders_query,
                                widget=Select2Widget(extra_classes="readonly"))} 

class OrderspecaView(ModelView):
    datamodel = SQLAInterface(Orderspeca)
    label_columns = {'orderheaders.id':'Order Header ID','sweetlevel':'sweetlevel (none/low/heavy)','icelevel':'icelevel (none/low/heavy)','ricelevel':'ricelevel (low/heavy)','drinkingstraw':'drinkingstraw (none)'}
    list_columns = ['id','orderheaders.id','sweetlevel','icelevel','ricelevel','drinkingstraw']
    edit_form_extra_fields = {'orderheaders':  QuerySelectField('Orderheaders',
                                query_factory=orderheaders_query,
                                widget=Select2Widget(extra_classes="readonly"))} 

class PaymethodsView(ModelView):
    datamodel = SQLAInterface(Paymethods)
    label_columns = {'orderheaders.Username':'Username','orderheaders.id':'Order Number','card_type':'card type (visa/master/tag & go)'}
    list_columns = ['id','orderheaders.id','orderheaders.Username','method','card_type']
    edit_form_extra_fields = {'orderheaders':  QuerySelectField('Orderheaders',
                                query_factory=orderheaders_query,
                                widget=Select2Widget(extra_classes="readonly"))}
class CouponsView(ModelView):
    datamodel = SQLAInterface(Coupons)
    label_columns = {'coupons_type':'card type (discount/birthday)'}
    list_columns = ['id','coupons_type','expire_date']
    edit_form_extra_fields = {'payments':  QuerySelectField('Payments',
                                query_factory=payments_query,
                                widget=Select2Widget(extra_classes="readonly"))}

class PaymentsView(ModelView):
    datamodel = SQLAInterface(Payments)
    label_columns = {'orderheaders.Username':'Username','orderheaders.id':'Order Number'}
    list_columns = ['id','orderheaders.id','orderheaders.Username','total_amount','status']
    edit_form_extra_fields = {'orderheaders':  QuerySelectField('Orderheaders',
                                query_factory=orderheaders_query,
                                widget=Select2Widget(extra_classes="readonly"))}
                                
    related_views = [CouponsView]                            

    
class OrderheadersView(ModelView):
    datamodel = SQLAInterface(Orderheaders)
    label_columns = {'Orderheaders':'Order Headers'}
    list_columns = ['id','Username','Location','Status','order_date']
  
    related_views = [OrderslinesView, OrderspecaView, TipView, RefundsView,PaymentsView,PaymethodsView]

"""Business"""

def commerces_query():
    return db.session.query(Commerces) 
    
class MonthreportView(ModelView):
    datamodel = SQLAInterface(Monthreport)
    label_columns = {'commerce.income':'Month income','commerce.date':'Date'}
    list_columns = ['id','commerce.income','commerce.date','status']
    edit_form_extra_fields = {'commerces':  QuerySelectField('Commerces',
                                query_factory=commerces_query,
                                widget=Select2Widget(extra_classes="readonly"))}    
 
class YearreportView(ModelView):
    datamodel = SQLAInterface(Yearreport)
    label_columns = {'commerce.income':'Year income','commerce.date':'Date'}
    list_columns = ['id','commerce.income','commerce.date','status']
    edit_form_extra_fields = {'commerces':  QuerySelectField('Commerces',
                                query_factory=commerces_query,
                                widget=Select2Widget(extra_classes="readonly"))}    
                                

class CommercesView(ModelView):
    datamodel = SQLAInterface(Commerces)
    label_columns = {'restaurant.name':'Restaurant Name','payments.id':'Payment id','payments.total_amount':'Total amount ( $HK )'}
    list_columns = ['id','restaurant.name','payments.id','payments.total_amount','date']
    edit_form_extra_fields = {'restaurant':  QuerySelectField("Restaurant",
                                query_factory=restaurant_query,
                                widget=Select2Widget(extra_classes="readonly"))}  
    edit_form_extra_fields = {'payments':  QuerySelectField('Payments',
                                query_factory=payments_query,
                                widget=Select2Widget(extra_classes="readonly"))}

    related_views = [MonthreportView]                            


  

"""deliveryboy"""

def deliveryman_query():
    return db.session.query(Deliveryman)



class IncomeView(ModelView):
      datamodel = SQLAInterface(Income)
      label_columns = {'Income':'Income'}
      list_columns = ['id','month','deliveryman.name','full_name','order_total','basic_salary']
     
      edit_form_extra_fields = {'deliveryman':  QuerySelectField("Deliveryman",
                                query_factory=deliveryman_query,
                                widget=Select2Widget(extra_classes="readonly"))}

class DeliverymanView(ModelView):
     datamodel = SQLAInterface(Deliveryman)
     list_columns = ['id','name','staff_number','condition','location','grade']
     related_views = [IncomeView]



def ranking_query():
    return db.session.query(Ranking)
"""test"""

class TestMView(ModelView):
    datamodel = SQLAInterface(test)

    label_columns = {'Restaurant':'Restaurant'}
    list_columns = ['name','address','Location','Telephone']
    

class TestView(BaseView):
    default_view = 'testview'
    @expose('/testview/')
    def testview(self):
        result = restaurant_query()
        self.update_redirect()
        return  self.render_template('testview.html',result = result)

class RanktableView(BaseView):
    default_view = 'ranktableview'
    @expose('/ranktableview/')
    def ranktableview(self):
        result = ranking_query()
        self.update_redirect()
        return  self.render_template('ranking.html',result = result)



db.create_all()


"""page view"""
appbuilder.add_view(VipView,'User', icon = "fa-address-book",category="User")
appbuilder.add_view(LiveView,'Address', icon = "fa-address-book",category="User")
appbuilder.add_view(CommentsView,'Comments', icon = "fa-address-book",category="User")
appbuilder.add_view(FavoriteView,'Favorite', icon = "fa-address-book",category="User")
appbuilder.add_view(ProfilesView,'Profiles', icon = "fa-address-book",category="User")
appbuilder.add_view(LogView,'Log', icon = "fa-address-book",category="User")


appbuilder.add_view(RestaurantView,"Restaurant",icon = "fa-cutlery", category = "Restaurant")
appbuilder.add_view(FoodtypeView,"Foods",icon = "fa-cutlery", category = "Restaurant")
appbuilder.add_view(FoodoptionView,"Food Option",icon = "fa-cutlery", category = "Restaurant")
appbuilder.add_view(NoticesView,"Notice",icon = "fa-cutlery", category = "Restaurant")
appbuilder.add_view(GradeView,"Restaurant grade",icon = "fa-cutlery", category = "Restaurant")
appbuilder.add_view(EventsView,"Special Event ",icon = "fa-cutlery", category = "Restaurant")
appbuilder.add_view(PromotionView,"Special Promotion ",icon = "fa-cutlery", category = "Restaurant")
appbuilder.add_view(OthervarietyView,"Other Variety ",icon = "fa-cutlery", category = "Restaurant")
appbuilder.add_view(CuisineView,"Cuisine ",icon = "fa-cutlery", category = "Restaurant")

appbuilder.add_view(RankingView,'Ranking', icon = "fa-cutlery",category="Restaurant")

appbuilder.add_view(CartheadersView,"Cart Header",icon = "fa-shopping-cart", category = "Cart")
appbuilder.add_view(CartlinesView,"Cart Line",icon = "fa-shopping-cart", category = "Cart")
appbuilder.add_view(SpecialneedsView,"Special Arrange",icon = "fa-shopping-cart", category = "Cart")

appbuilder.add_view(OrderheadersView,"Order Header",icon = "fa-shopping-cart", category = "Order")
appbuilder.add_view(OrderslinesView,"Order Line",icon = "fa-shopping-cart", category = "Order")
appbuilder.add_view(OrderspecaView,"Order Special Arrange",icon = "fa-shopping-cart", category = "Order")
appbuilder.add_view(TipView,"Tip",icon ="fa-shopping-cart", category = "Order")     
appbuilder.add_view(OrderhistorysView,"Order Historys",icon = "fa-shopping-cart", category = "Order")   
appbuilder.add_view(RefundsView,"Refunds",icon = "fa-shopping-cart", category = "Order")  

appbuilder.add_view(PaymentsView,"Payment",icon = "fa-shopping-cart", category = "Payment")  
appbuilder.add_view(PaymethodsView,"Pay method",icon = "fa-shopping-cart", category = "Payment")  
appbuilder.add_view(CouponsView,"Coupon",icon = "fa-shopping-cart", category = "Payment")  

appbuilder.add_view(CommercesView,"Business",icon = "fa-shopping-cart", category = "Business")  
appbuilder.add_view(MonthreportView,"Month Report",icon = "fa-shopping-cart", category = "Business")  
appbuilder.add_view(YearreportView,"Year Report",icon = "fa-shopping-cart", category = "Business")  


appbuilder.add_view(DeliverymanView,'Delivery Man', icon = "fa-address-card-o",category="DeliveryStaff")
appbuilder.add_view(IncomeView,'Income', icon = "fa-address-card-o",category="DeliveryStaff")

appbuilder.add_view(TestView,'testview', icon = "fa-address-card-o",category="test")
# appbuilder.add_view(TestMView,"testMView",icon = "fa-address-card-o",category = "test")
appbuilder.add_view(RanktableView,"Ranking View",icon = "fa-address-card-o",category = "test")

