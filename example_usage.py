from client import SplitShipmentWarehouseDistanceMinimizerClient

def main():
    client = SplitShipmentWarehouseDistanceMinimizerClient()
    res = client.optimize_fulfillment_split('10001', ['SKU-JACKET'])
    print('Split Shipment Minimizer: ' + res['routing_plan_id'] + ' (' + res['assigned_warehouse'] + ')')
    print('Distance: ' + str(res['transit_distance_miles']) + ' miles | Splits: ' + str(res['split_shipments_count']))
    print('Manifest URL: ' + res['manifest_dispatch_url'])

if __name__ == '__main__':
    main()
