import datetime, pytz

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text 
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
from flask_sqlalchemy import SQLAlchemy



def today():
   return datetime.datetime.today().strftime("%Y-%m-%d %H:%M" )
 
def now():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("Asia/Hong_Kong"))
    return pst_now.strftime("%B %d, %Y %H:%M" )    
   
# def now():
#   return datetime.datetime.now().strftime("%B %d, %Y %H:%M" )   

################################    REAL Table    ############################################################        
        
        
class Vip(Model):
        id = Column(Integer,primary_key=True)
        name = Column(String(50), unique=True, nullable=False)
        password = Column(String(255), nullable=False)
        role = Column(String(20), nullable=False)
            
        def __repr__(self):
            return self.name
        
        
class Live(Model):
        id = Column(Integer,primary_key=True)
        vip_id = Column(Integer,ForeignKey('vip.id'), nullable=False)
        vip = relationship("Vip")
        address = Column(String(255), nullable=False)
        note = Column(String(255), nullable=True)
    
        def __repr__(self):
            return "%s-%s" % (self.address, self.note)
           
class Log(Model):
        id = Column(Integer,primary_key=True)
        vip_id = Column(Integer,ForeignKey('vip.id'), nullable=False)
        vip = relationship("Vip")
        date_in = Column(String(30), default=today, nullable=False)
        
        def __repr__(self):
             return self.date_in

class Comments(Model):
        id = Column(Integer,primary_key=True)
        vip_id = Column(Integer,ForeignKey('vip.id'), nullable=False)
        vip = relationship("Vip")
        text = Column(Text, nullable=False)
    
        def __repr__(self):
            return self.text
        
        
        
class Profiles(Model):
        id = Column(Integer,primary_key=True)
        vip_id = Column(Integer,ForeignKey('vip.id'), nullable=False)
        vip = relationship("Vip")
        tel_no = Column(Integer, nullable=False)
        email = Column(String(100), nullable=False)

        def __repr__(self):
            return self.tel_no
            
        
class Favorite(Model):
        id = Column(Integer,primary_key=True)
        vip_id = Column(Integer,ForeignKey('vip.id'), nullable=False)
        vip = relationship("Vip")
        restaurant_name = Column(String(100), nullable=True)
    
        def __repr__(self):
            return self.restaurant_name
        
 #############################################################################################################################################

class Restaurant(Model):
        id = Column(Integer,primary_key=True)
        name = Column(String(50), unique=False, nullable=False)
        location = Column(String(255), nullable=True)
        address = Column(String(20), nullable=True)
        tel_number = Column(String(20), nullable=True)
        category = Column(String(20), nullable=True)
        collection_point = Column(String(20))
            
        def __repr__(self):
            return"%s-%s" % (self.name, self.location)
            
class Foodtype(Model):
        id = Column(Integer,primary_key=True)
        item_name = Column(String(20),nullable=False)
        description = Column(String(20), nullable=True)
        price = Column(Integer, nullable=True)
        restaurant_id = Column(Integer,ForeignKey('restaurant.id'), nullable=False)
        restaurant = relationship("Restaurant")
    
        def __repr__(self):
            return "%s-%int" % (self.item_name, self.price)
            
class Foodoption(Model):
        id = Column(Integer,primary_key=True)
        option_name = Column(String(50),nullable=False)
        restaurant_id = Column(Integer,ForeignKey('restaurant.id'), nullable=False)
        restaurant = relationship("Restaurant")
    
        def __repr__(self):
            return self.option_name 
            
class Notices(Model):
        id = Column(Integer,primary_key=True)
        notice = Column(String(100),nullable=True)
        restaurant_id = Column(Integer,ForeignKey('restaurant.id'), nullable=False)
        restaurant = relationship("Restaurant")
    
        def __repr__(self):
            return self.item_notice           
            
class Grade(Model):
        id = Column(Integer,primary_key=True)
        grade = Column(String(50),nullable=False)
        restaurant_id = Column(Integer,ForeignKey('restaurant.id'), nullable=False)
        restaurant = relationship("Restaurant")
    
        def __repr__(self):
            return self.grade   
            
class Promotion(Model):
        id = Column(Integer,primary_key=True)
        discount = Column(Integer,nullable=True)
        restaurant_id = Column(Integer,ForeignKey('restaurant.id'), nullable=False)
        restaurant = relationship("Restaurant")
    
        def __repr__(self):
            return self.discount   
            
class Events(Model):
        id = Column(Integer,primary_key=True)
        event_name = Column(String(50),nullable=True)
        start_date = Column(Date,default=now , nullable=True)
        end_date = Column(Date,default=now , nullable=True)
        restaurant_id = Column(Integer,ForeignKey('restaurant.id'), nullable=False)
        restaurant = relationship("Restaurant")
    
        def __repr__(self):
            return "%s-%datetime-%datetime" % (self.event_name, self.start_date, self.end_date)  
            
class Othervariety(Model):
        id = Column(Integer,primary_key=True)
        item_name = Column(String(50),nullable=True)
        restaurant_id = Column(Integer,ForeignKey('restaurant.id'), nullable=False)
        restaurant = relationship("Restaurant")
    
        def __repr__(self):
            return self.item_name
            
class Cuisine(Model):
        id = Column(Integer,primary_key=True)
        item_name = Column(String(50),nullable=True)
        restaurant_id = Column(Integer,ForeignKey('restaurant.id'), nullable=False)
        restaurant = relationship("Restaurant")
    
        def __repr__(self):
            return self.item_name            
            

# #####################################################################################################################################################################
  
class Pay(Model):
    id = Column(Integer, primary_key=True )
    total_amount = Column(Integer , nullable=True)
    status = Column(String(50),nullable=True)
    orderedheader_id = Column(Integer, ForeignKey('orderedheader.id'), nullable=False)
    orderedheader = relationship("Orderedheader")
   
    def __repr__(self):
        return "%int-%int-%s" % (self.id,self.total_amount, self.status)   
    
class Paysmethod(Model):
    id = Column(Integer,primary_key=True)
    method = Column(String(10), nullable=False)
    card_type = Column(String(10), nullable=True)
    orderedheader_id = Column(Integer, ForeignKey('orderedheader.id'), nullable=False)
    orderedheader = relationship("Orderedheader")
    
    def __repr__(self):
        return "%s-%s" % (self.method, self.card_type)   
        
class Couponss(Model):
    id = Column(Integer,primary_key=True)
    coupons_type = Column(String(10), nullable=True)
    expire_date = Column(Date, nullable=True)
    pay_id = Column(Integer, ForeignKey('pay.id'), nullable=False)
    pay = relationship("Pay")
    
    def __repr__(self):
        return "%s-%datetime" % (self.coupons_type, self.expire_date)  
        
        
class Commercess(Model):
    id = Column(Integer,primary_key=True)
    income = Column(Integer, nullable = True)
    restaurant_id = Column(Integer,ForeignKey('restaurant.id'), nullable=False)
    restaurant = relationship("Restaurant")
    pay_id = Column(Integer, ForeignKey('pay.id'), nullable=False)
    pay = relationship("Pay")
    date = Column(String(30),default=now , nullable=True)
    
    
    def __repr__(self):
        return "%int-%s" % (self.income, self.date) 
        
class Monthreports(Model):
    id = Column(Integer,primary_key=True)
    commercess_id = Column(Integer,ForeignKey('commercess.id'), nullable=False)
    commercess = relationship("Commercess")
    status = Column(String(20), nullable=False)
    
    def __repr__(self):
        return self.status
        
class Yearreports(Model):
    id = Column(Integer,primary_key=True)
    commercess_id = Column(Integer,ForeignKey('commercess.id'), nullable=False)
    commercess = relationship("Commercess")
    status = Column(String(20), nullable=False)
    
    def __repr__(self):
        return self.status
    

# #################################################################################################################################################

        
class Orderedheader(Model):
    id = Column(Integer, primary_key=True )
    Username = Column(String(20),nullable=False)
    Location = Column(String(50), nullable=False)
    Status = Column(String(20), nullable=True)
    Deliveryman = Column(String(20), nullable=True)
    order_date = Column(String(30),default=now ,nullable=False)  
    
    def __repr__(self):
        return "%s-%int-%s-%s" % (self.Username,self.id, self.Location, self.Status)
        
class Orderedline(Model):
    id = Column(Integer, primary_key=True )
    item_name = Column(String(50), nullable=False)
    description = Column(String(50), nullable=True)
    price = Column(Integer ,nullable=False)
    orderedheader_id = Column(Integer, ForeignKey('orderedheader.id'), nullable=False)
    orderedheader = relationship("Orderedheader")
    restaurant_id = Column(Integer,ForeignKey('restaurant.id'), nullable=False)
    restaurant = relationship("Restaurant")
    
    def __repr__(self):
        return "%s-%s-%int" % (self.item_name, self.description, self.price)
        
class Tipss(Model):
    id = Column(Integer, primary_key=True )
    tip_comment = Column(String(50), nullable=True)
    tip = Column(Integer ,nullable=True)
    orderedheader_id = Column(Integer, ForeignKey('orderedheader.id'), nullable=False)
    orderedheader = relationship("Orderedheader")
  
    def __repr__(self):
        return self.tip

class Orderhistoryss(Model):
    id = Column(Integer, primary_key=True )
    orderedheader_id = Column(Integer, ForeignKey('orderedheader.id'), nullable=False)
    orderedheader = relationship("Orderedheader")
   
     
   
class Refundss(Model):
    id = Column(Integer, primary_key=True )
    amount = Column(Integer , nullable=True)
    status = Column(String(50),nullable=True)
    refund_date = Column(String(30),default=today ,nullable=False)
    orderedheader_id = Column(Integer, ForeignKey('orderedheader.id'), nullable=False)
    orderedheader = relationship("Orderedheader")
   
    def __repr__(self):
        return "%int-%s-%date" % (self.amount, self.status, self.refund_date)   
        
    
class Ranking(Model):
    id = Column(Integer,primary_key=True)
    rank = Column(Integer, nullable=True)
    total_order = Column(Integer, nullable=True)
    Restaurant_name = Column(String(255), nullable = True)
    
    def __repr__(self):
        return self.Restaurant_name
        
class Ordersspecial(Model):
    id = Column(Integer, primary_key=True )
    sweetlevel = Column(String(50), nullable=False)
    icelevel = Column(String(50), nullable=False)
    ricelevel = Column(String(50), nullable=False)
    drinkingstraw = Column(String(50), nullable=False)
    orderedheader_id = Column(Integer, ForeignKey('orderedheader.id'), nullable=False)
    orderedheader = relationship("Orderedheader")
  
    def __repr__(self):
        return "%s-%s-%s-%s" % (self.sweetlevel, self.icelevel, self.ricelevel, self.drinkingstraw)

        
# #######################################################################################################################################################



class Deliveryman(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    staff_number = Column(Integer, nullable=True)
    condition = Column(String(255), nullable = True)
    location = Column(String(100), nullable=True)
    grade = Column(String(10), nullable=True)
    
    def __repr__(self):
        return self.name

class Income(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=True)
    basic_salary = Column(Integer, nullable=True)
    order_total = Column(Integer, nullable=True)
    month = Column(Integer, nullable=False)
    deliveryman_id = Column(Integer, ForeignKey('deliveryman.id'), nullable=False)
    deliveryman = relationship("Deliveryman")
    

    def __repr__(self):
        return self.full_name

         
#Basketheader area#############################################################################################

class Cartheaders(Model):
    id = Column(Integer, primary_key=True )
    username = Column(String(20),nullable=False)
    Collectlocation = Column(String(50), nullable=False)
    Cart_date = Column(String(30),default=today ,nullable=False)  
    
    def __repr__(self):
        return "%s-%int-%s" % (self.username,self.id, self.Collectlocation)
        
class Cartslines(Model):
    id = Column(Integer, primary_key=True )
    item_name = Column(String(50), nullable=False)
    description = Column(String(20), nullable=False)
    price = Column(Integer ,nullable=False)
    cartheaders_id = Column(Integer, ForeignKey('cartheaders.id'), nullable=False)
    cartheaders = relationship("Cartheaders")
    restaurant_id = Column(Integer,ForeignKey('restaurant.id'), nullable=False)
    restaurant = relationship("Restaurant")
    
    def __repr__(self):
        return "%s-%s-%int" % (self.item_name, self.description, self.price)
        
class Specialneeds(Model):
    id = Column(Integer, primary_key=True )
    sweetlevel = Column(String(50), nullable=False)
    icelevel = Column(String(50), nullable=False)
    ricelevel = Column(String(50), nullable=False)
    drinkingstraw = Column(String(50), nullable=False)
    cartheaders_id = Column(Integer, ForeignKey('cartheaders.id'), nullable=False)
    cartheaders = relationship("Cartheaders")
  
    def __repr__(self):
        return "%s-%s-%s-%s" % (self.sweetlevel, self.icelevel, self.ricelevel, self.drinkingstraw)

# #######################################################################################
    
    
    
    
    
   

    
    
