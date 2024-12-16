from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher

# Existing mapping for inventory
listing_to_item_mapping = {
    "L0001": "ITM00001",  # Example mapping
    "L0002": "ITM00002",
    "L0003": "ITM00003",
}

class ActionCheckInventory(Action):
    def name(self):
        return "action_check_inventory"

    def run(self, dispatcher, tracker, domain):
        listing_id = tracker.get_slot("listing_id")
        if not listing_id:
            dispatcher.utter_message("Please provide the listing ID.")
            return []

        # Simulated inventory check
        item_id = listing_to_item_mapping.get(listing_id)
        if item_id:
            dispatcher.utter_message(f"The listing {listing_id} is available!")
        else:
            dispatcher.utter_message(f"Sorry, listing {listing_id} is not available.")
        return []

class ActionProvidePickupAddress(Action):
    def name(self):
        return "action_provide_pickup_address"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("The pickup address is: 123 Marketplace Street, City Center.")
        return []

class ActionProvidePickupTiming(Action):
    def name(self):
        return "action_provide_pickup_timing"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Pickup is available from 9 AM to 6 PM, Monday to Saturday.")
        return []
