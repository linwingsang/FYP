from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_appbuilder.baseviews import expose, BaseView
from . import appbuilder, db
from .models import test,Deliveryman,Income,Vip,Live,Log,Comments,Profiles,Favorite,Ranking
from .models import Orderedheader,Orderedline,Tipss, Orderhistoryss, Refundss, Ordersspecial
from .models import Cartheaders,Cartslines,Specialneeds,Restaurant,Foodtype,Foodoption,Notices,Grade,Promotion,Events,Othervariety,Cuisine
from .models import Pay, Paysmethod, Couponss, Commercess, Monthreports, Yearreports
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
     show_template = 'appbuilder/general/model/show_cascade.html'
     edit_template = 'appbuilder/general/model/edit_cascade.html'

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
     show_template = 'appbuilder/general/model/show_cascade.html'
     edit_template = 'appbuilder/general/model/edit_cascade.html'


class RankingView(ModelView):
     datamodel = SQLAInterface(Ranking)
     label_columns = {'Restaurant_name':'Restaurant'}
     list_columns = ['rank','Restaurant_name','total_order']

"""basket"""
def cartheaders_query():
    return db.session.query(Cartheaders)

class CartslinesView(ModelView):
    datamodel = SQLAInterface(Cartslines)
    label_columns = {'price':'price ($HK)','cartheaders.id':'Cart Header ID'}
    list_columns = ['id','cartheaders.id','restaurant.name', 'item_name','description','price']
    edit_form_extra_fields = {'cartheaders':  QuerySelectField('Cartheaders',
                                query_factory=cartheaders_query,
                                widget=Select2Widget(extra_classes="readonly"))}
    edit_form_extra_fields = {'restaurant':  QuerySelectField("Restaurant",
                                query_factory=restaurant_query,
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
  
    related_views = [CartslinesView, SpecialneedsView]
    show_template = 'appbuilder/general/model/show_cascade.html'
    edit_template = 'appbuilder/general/model/edit_cascade.html'

"""order"""
   
def orderedheader_query():
    return db.session.query(Orderedheader)
    
def pay_query():
    return db.session.query(Pay)    
    
class OrderedlineView(ModelView):
    datamodel = SQLAInterface(Orderedline)
    list_columns = ['id','orderedheader.id','restaurant.name', 'item_name','description','price']
    edit_form_extra_fields = {'orderedheader':  QuerySelectField('Orderedheader',
                                query_factory=orderedheader_query,
                                widget=Select2Widget(extra_classes="readonly"))}
    edit_form_extra_fields = {'restaurant':  QuerySelectField("Restaurant",
                                query_factory=restaurant_query,
                                widget=Select2Widget(extra_classes="readonly"))}   
        
class TipssView(ModelView):
    datamodel = SQLAInterface(Tipss)
    label_columns = {'tip':'Tips ($HK)'}
    list_columns = ['id','orderedheader.id', 'tip','tip_comment']
    edit_form_extra_fields = {'orderedheader':  QuerySelectField('Orderedheader',
                                query_factory=orderedheader_query,
                                widget=Select2Widget(extra_classes="readonly"))}

class OrderhistoryssView(ModelView):
    datamodel = SQLAInterface(Orderhistoryss)
    list_columns = ['id','orderedheader.id']
    edit_form_extra_fields = {'orderedheader':  QuerySelectField('Orderedheader',
                                query_factory=orderedheader_query,
                                widget=Select2Widget(extra_classes="readonly"))}
                
class RefundssView(ModelView):
    datamodel = SQLAInterface(Refundss)
    label_columns = {'orderedheader.Username':'Username','orderedheader.id':'Order Number'}
    list_columns = ['id','orderedheader.id','orderedheader.Username','amount','status','refund_date']
    edit_form_extra_fields = {'orderedheader':  QuerySelectField('Orderedheader',
                                query_factory=orderedheader_query,
                                widget=Select2Widget(extra_classes="readonly"))} 

class OrdersspecialView(ModelView):
    datamodel = SQLAInterface(Ordersspecial)
    label_columns = {'orderedheader.id':'Order Header ID','sweetlevel':'sweetlevel (none/low/heavy)','icelevel':'icelevel (none/low/heavy)','ricelevel':'ricelevel (low/heavy)','drinkingstraw':'drinkingstraw (none)'}
    list_columns = ['id','orderedheader.id','sweetlevel','icelevel','ricelevel','drinkingstraw']
    edit_form_extra_fields = {'orderedheader':  QuerySelectField('Orderedheader',
                                query_factory=orderedheader_query,
                                widget=Select2Widget(extra_classes="readonly"))} 

class PaysmethodView(ModelView):
    datamodel = SQLAInterface(Paysmethod)
    label_columns = {'orderedheader.Username':'Username','orderedheader.id':'Order Number','card_type':'card type (visa/master/tag & go)'}
    list_columns = ['id','orderedheader.id','orderedheader.Username','method','card_type']
    edit_form_extra_fields = {'orderedheader':  QuerySelectField('Orderedheader',
                                query_factory=orderedheader_query,
                                widget=Select2Widget(extra_classes="readonly"))}
class CouponssView(ModelView):
    datamodel = SQLAInterface(Couponss)
    label_columns = {'coupons_type':'card type (discount/birthday)'}
    list_columns = ['id','coupons_type','expire_date']
    edit_form_extra_fields = {'pay':  QuerySelectField('Pay',
                                query_factory=pay_query,
                                widget=Select2Widget(extra_classes="readonly"))}

class PayView(ModelView):
    datamodel = SQLAInterface(Pay)
    label_columns = {'orderedheader.Username':'Username','orderedheader.id':'Order Number'}
    list_columns = ['id','orderedheader.id','orderedheader.Username','total_amount','status']
    edit_form_extra_fields = {'orderedheader':  QuerySelectField('Orderedheader',
                                query_factory=orderedheader_query,
                                widget=Select2Widget(extra_classes="readonly"))}
                                
    related_views = [CouponssView]                            

    
class OrderedheaderView(ModelView):
    datamodel = SQLAInterface(Orderedheader)
    label_columns = {'Orderedheader':'Order Headers'}
    list_columns = ['id','Username','Location','Status','Deliveryman','order_date']
  
    related_views = [OrderedlineView,OrdersspecialView,TipssView,PayView,PaysmethodView,RefundssView]
    show_template = 'appbuilder/general/model/show_cascade.html'
    edit_template = 'appbuilder/general/model/edit_cascade.html'

"""Business"""

def commercess_query():
    return db.session.query(Commercess) 
    
class MonthreportsView(ModelView):
    datamodel = SQLAInterface(Monthreports)
    label_columns = {'commercess.income':'Month income','commerce.date':'Date'}
    list_columns = ['id','commercess.income','commercess.date','status']
    edit_form_extra_fields = {'commercess':  QuerySelectField('Commercess',
                                query_factory=commercess_query,
                                widget=Select2Widget(extra_classes="readonly"))}    
 
class YearreportsView(ModelView):
    datamodel = SQLAInterface(Yearreports)
    label_columns = {'commercess.income':'Year income','commercess.date':'Date'}
    list_columns = ['id','commercess.income','commercess.date','status']
    edit_form_extra_fields = {'commercess':  QuerySelectField('Commercess',
                                query_factory=commercess_query,
                                widget=Select2Widget(extra_classes="readonly"))}    
                                

class CommercessView(ModelView):
    datamodel = SQLAInterface(Commercess)
    label_columns = {'restaurant.name':'Restaurant Name','pay.id':'Payment id','pay.total_amount':'Total amount ( $HK )'}
    list_columns = ['id','restaurant.name','pay.id','pay.total_amount','date']
    edit_form_extra_fields = {'restaurant':  QuerySelectField("Restaurant",
                                query_factory=restaurant_query,
                                widget=Select2Widget(extra_classes="readonly"))}  
    edit_form_extra_fields = {'pay':  QuerySelectField('Pay',
                                query_factory=pay_query,
                                widget=Select2Widget(extra_classes="readonly"))}

    related_views = [MonthreportsView,YearreportsView]
    show_template = 'appbuilder/general/model/show_cascade.html'
    edit_template = 'appbuilder/general/model/edit_cascade.html'


  

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
     show_template = 'appbuilder/general/model/show_cascade.html'
     edit_template = 'appbuilder/general/model/edit_cascade.html'

"""test"""

def ranking_query():
    return db.session.query(Ranking)

def comments_query():
    return db.session.query(Comments)

def foodtype_query():
    return db.session.query(Foodtype)
    
def cartsline_add():
    return db.session.add(Cartslines)


class CartslineView(BaseView):
    default_view = 'cartslineview'
    @expose('/Cartslineview/<int:id>')
    def add(self,id):
        items = foodtype_query()
        for item in items :
            if item.id == id :
                 item_name = item.item_name
                 description = item.description
                 price = item.price
                 restaurant_id = item.restaurant_id
        cartsline_add()   
        self.update_redirect()
        return  self.render_template('cartadd.html')    
    
class SkwView(BaseView):
    default_view = 'skwview'
    @expose('/skwview/')
    def skwview(self):
        result = restaurant_query()
        self.update_redirect()
        return  self.render_template('skw.html',result = result)

class TkoView(BaseView):
    default_view = 'tkoview'
    @expose('/tkoview/')
    def tkoview(self):
        result = restaurant_query()
        self.update_redirect()
        return  self.render_template('tko.html',result = result)

class YlView(BaseView):
    default_view = 'ylview'
    @expose('/ylview/')
    def ylview(self):
        result = restaurant_query()
        self.update_redirect()
        return  self.render_template('yl.html',result = result)
        
class ShopView(BaseView):
    default_view ='shopview1'
    @expose('/shopview1/')
    def shopview1(self):
        shopid = 1
        result = foodtype_query()
        shop = restaurant_query()
        self.update_redirect()
        return  self.render_template('shop1.html',result = result, shopid = shopid, shop = shop)

   
    @expose('/shopview2/')
    def shopview2(self):
        shopid = 2
        result = foodtype_query()
        shop = restaurant_query()
        self.update_redirect()
        return  self.render_template('shop2.html',result = result, shopid = shopid, shop = shop)


    @expose('/shopview3/')
    def shopview3(self):
        shopid = 3
        result = foodtype_query()
        shop = restaurant_query()
        self.update_redirect()
        return  self.render_template('shop3.html',result = result, shopid = shopid, shop=shop)


    @expose('/shopview4/')
    def shopview4(self):
        shopid = 4
        result = foodtype_query()
        shop = restaurant_query()
        self.update_redirect()
        return  self.render_template('shop4.html',result = result, shopid = shopid, shop=shop)


class RanktableView(BaseView):
    default_view = 'ranktableview'
    @expose('/ranktableview/')
    def ranktableview(self):
        result = ranking_query()
        self.update_redirect()
        return  self.render_template('ranking.html',result = result)

class CommentView(BaseView):
    default_view = 'commentview'
    @expose('/commentview/')
    def commentview(self):
        result = comments_query()
        self.update_redirect()
        return  self.render_template('comment.html',result = result)





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
appbuilder.add_view(CartslinesView,"Cart Line",icon = "fa-shopping-cart", category = "Cart")
appbuilder.add_view(SpecialneedsView,"Special Arrange",icon = "fa-shopping-cart", category = "Cart")

appbuilder.add_view(OrderedheaderView,"Order Header",icon = "fa-shopping-cart", category = "Order")
appbuilder.add_view(OrderedlineView,"Order Line",icon = "fa-shopping-cart", category = "Order")
appbuilder.add_view(OrdersspecialView,"Order Special Arrange",icon = "fa-shopping-cart", category = "Order")
appbuilder.add_view(TipssView,"Tip",icon ="fa-shopping-cart", category = "Order")     
appbuilder.add_view(OrderhistoryssView,"Order Historys",icon = "fa-shopping-cart", category = "Order")   
appbuilder.add_view(RefundssView,"Refunds",icon = "fa-shopping-cart", category = "Order")  

appbuilder.add_view(PayView,"Payment",icon = "fa-shopping-cart", category = "Payment")  
appbuilder.add_view(PaysmethodView,"Pay method",icon = "fa-shopping-cart", category = "Payment")  
appbuilder.add_view(CouponssView,"Coupon",icon = "fa-shopping-cart", category = "Payment")  

appbuilder.add_view(CommercessView,"Business",icon = "fa-shopping-cart", category = "Business")  
appbuilder.add_view(MonthreportsView,"Month Report",icon = "fa-shopping-cart", category = "Business")  
appbuilder.add_view(YearreportsView,"Year Report",icon = "fa-shopping-cart", category = "Business")  

appbuilder.add_view(DeliverymanView,'Delivery Man', icon = "fa-address-card-o",category="DeliveryStaff")
appbuilder.add_view(IncomeView,'Income', icon = "fa-address-card-o",category="DeliveryStaff")

appbuilder.add_view(ShopView,'Shop view1', icon = "fa-address-card-o",category="test")
appbuilder.add_link("Shop view2", href="/shopview/shopview2/", category="test")
appbuilder.add_link("Shop view3", href="/shopview/shopview3/", category="test")
appbuilder.add_link("Shop view4", href="/shopview/shopview4/", category="test")
appbuilder.add_view(YlView,'YL view', icon = "fa-address-card-o",category="test")
appbuilder.add_view(TkoView,'TKO view', icon = "fa-address-card-o",category="test")
appbuilder.add_view(SkwView,'SKW view', icon = "fa-address-card-o",category="test")
appbuilder.add_view(RanktableView,"Ranking View",icon = "fa-address-card-o",category = "test")
appbuilder.add_view(CommentView,"Comment View",icon = "fa-address-card-o",category = "test")
