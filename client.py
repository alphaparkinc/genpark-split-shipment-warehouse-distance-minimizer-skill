class SplitShipmentWarehouseDistanceMinimizerClient:
    def optimize_fulfillment_split(self, destination_zip='94105', order_skus=['SKU-MATTRESS-QUEEN', 'SKU-PILLOW-SET']):
        return {
            'routing_plan_id': 'ful_rte_9918',
            'destination_zip': destination_zip,
            'fulfillment_strategy': 'SINGLE_ORIGIN_OPTIMAL_HUB',
            'assigned_warehouse': 'OAKLAND_CALIFORNIA_HUB',
            'transit_distance_miles': 14.8,
            'split_shipments_count': 1,
            'estimated_carrier_cost_usd': 18.50,
            'carbon_emission_grams': 1240,
            'manifest_dispatch_url': 'https://shipbob.logistics.genpark.ai/routes/9918.json'
        }
