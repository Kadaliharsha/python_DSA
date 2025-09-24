import heapq

class ParkingLot:
    def __init__(self, slots):
        self.slots = {i: None for i in range(1, slots + 1)}
        self.available_slots = list(self.slots.keys())
        heapq.heapify(self.available_slots)

    def park(self, reg_no):
        if not self.available_slots:
            print("Parking is full")
            return

        slot = heapq.heappop(self.available_slots)
        self.slots[slot] = reg_no
        print(f"Car {reg_no} parked at slot {slot}")

    def leave(self, slot):
        if slot not in self.slots:
            print(f"Invalid slot {slot}")
        elif self.slots[slot] is None:
            print(f"Slot {slot} already empty")
        else:
            print(f"Car {self.slots[slot]} left slot {slot}")
            self.slots[slot] = None
            heapq.heappush(self.available_slots, slot)
            
    def status(self):
        print("Slot No. | Registration No.")
        for slot, car in self.slots.items():
            if car is not None:
                print(f"{slot} | {car}")
        return
    
    def search(self, reg_no):
        for slot, car in self.slots.items():
            if car == reg_no:
                print(f"Car {reg_no} is parked at slot {slot}")
                return
        print(f"Car {reg_no} not found in the parking lot")
    
if __name__ == "__main__":
    lot = ParkingLot(3)
    lot.park("KA-01-HH-1234")
    lot.park("KA-01-HH-9999")
    lot.status()
    lot.leave(1)
    lot.status()
    lot.search("KA-01-HH-1234")
    lot.search("KA-01-HH-1235")
