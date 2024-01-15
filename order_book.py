from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Base, Order

engine = create_engine('sqlite:///orders.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def process_order(order):
	# Your code here
	# insert the order into the "Order" table
	ed_order = Order(sender_pk=order['sender_pk'], receiver_pk=order['receiver_pk'], buy_currency=order['buy_currency'],sell_currency=order['sell_currency'], buy_amount=order['buy_amount'],sell_amount=order['sell_amount'])
	if 'creator_id' in order.keys():
		ed_order.creator_id = order['creator_id']
		
	
	session.add(ed_order)
	session.commit()

	imp_exchange_rate = order['sell_amount'] / order['buy_amount']
	

	# check if there are any existing orders that match the new order
	orders = session.query(Order).filter(Order.filled == None).all()    #get all unfilled orders
	#print(orders)
	for o in orders:
		if ((o.buy_currency == ed_order.sell_currency) and (o.sell_currency == ed_order.buy_currency)):
			if imp_exchange_rate >= o.buy_amount / o.sell_amount:
				
				# a match is found
				# set the tfilled field to be the current timestamp
				o.filled = datetime.now()
				ed_order.filled = o.filled

				# set counterpartyid to be the id of the each other
				ed_order.counterparty_id = o.id
				o.counterparty_id = ed_order.id
				session.commit()
				# if one of the order is not completely filled, get the derived order
				if (ed_order.buy_amount > o.sell_amount):
					child_order_buy = ed_order.buy_amount - o.sell_amount
					child_order_sell = child_order_buy * imp_exchange_rate
					child_creater_id = ed_order.id
					child_order_dict = {'sender_pk': ed_order.sender_pk, 'receiver_pk': ed_order.receiver_pk,'buy_currency': ed_order.buy_currency, 'sell_currency': ed_order.sell_currency,'buy_amount': child_order_buy, 'sell_amount': child_order_sell,'creator_id': child_creater_id}
					#ed_order.child = child_order
					#session.commit()
					process_order(child_order_dict)
					#session.commit()
				if (ed_order.sell_amount < o.buy_amount):
					child_order_buy = o.buy_amount - ed_order.sell_amount
					child_order_sell = (child_order_buy * o.sell_amount) / o.buy_amount
					child_creater_id = o.id
					child_order_dict = {'sender_pk': o.sender_pk, 'receiver_pk': o.receiver_pk,'buy_currency': o.buy_currency, 'sell_currency': o.sell_currency,'buy_amount': child_order_buy, 'sell_amount': child_order_sell,'creator_id': child_creater_id}
					#o.child = child_order
					#session.commit()
					process_order(child_order_dict)
					#session.commit()

			break  
    		
    


