import csv
quantity_by_driver = {}
with open('data/shipping_data_0.csv', newline='') as csvfile:
    shipping_0 = csv.DictReader(csvfile, delimiter=',')
    count = 0
    for row in shipping_0:
        driver_id = row['driver_identifier']
        quantity_by_driver[driver_id] = row['product_quantity']
        #shipment[row['product_quantity']] = row
        # print(f"QUANTITY: {row['product_quantity']}")
        # count += 1
        # if count == 2:
        #     break

product_info = {}
with open('data/shipping_data_1.csv', newline='') as csvfile:
    shipment_Id1 = csv.DictReader(csvfile, delimiter=',')
    count = 0
    for row in shipment_Id1:
        sid = row['shipment_identifier']
        product_info[sid] = {
            'product': row['product'],
            'on_time': row['on_time']
        }

        # shipment[row['shipment_identifier']] = row
        # print(f"SHIPMENT IDENTIFER: {row['shipment_identifier']}")
        # count += 1
        # if count == 2:
        #     break

with open('data/shipping_data_2.csv', newline='') as csvfile:
    shipment_Id2 = csv.DictReader(csvfile, delimiter=',')
    count = 0
    for row in shipment_Id2:
        shipment_id = row['shipment_identifier']
        origin = row['origin_warehouse']
        destination = row['destination_store']
        driver = row['driver_identifier']

        product_data = product_info.get(shipment_id,{})
        quantity = quantity_by_driver.get(driver,'N/A')
        
        print(
            f"SHIPMENT_ID: {sid} | "
            f"PRODUCT: {product_data.get('product', 'N/A')} | "
            f"QUANTITY: {quantity} | "
            f"ON_TIME: {product_data.get('on_time', 'N/A')} | "
            f"ORIGIN: {origin} | "
            f"DESTINATION: {destination} | "
            f"DRIVER: {driver}"
        )
        count += 1
        if count == 5:
            break
        # shipment_Id = shipment.get(row['shipment_identifier'])
        # quantity = shipment.get(row['product_quantity'])
        # if shipment_Id:
        #     print(f"SHIPMENT_ID: {row['shipment_identifier']}"
        #         f" DESTINATION: {row['destination_store']}"
        #         f" PRODUCT: {shipment_Id['product']}"
        #         f" ON TIME: {shipment_Id['on_time']}"
        #         f" QUANTITY: {quantity['product_quantity']}"
        #         )
            

        


    


        
