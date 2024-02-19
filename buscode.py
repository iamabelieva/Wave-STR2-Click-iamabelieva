class Bus:
    def _init_(self, fare):
        self.fare = fare
        self.passenger_count = 0
        self.total_revenue = 0

    def board_passenger(self, cash):
        if cash >= self.fare:
            self.passenger_count += 1
            self.total_revenue += self.fare
            return True
        else:
            return False

    def display_stats(self):
        print(f"Passenger count: {self.passenger_count}")
        print(f"Total revenue: ${self.total_revenue}")


# Example usage:
bus = Bus(fare=5)

cash1 = 7
if bus.board_passenger(cash1):
    print(f"Boarded passenger with ${cash1} cash.")
else:
    print(f"Not enough cash to board with ${cash1}.")

cash2 = 4
if bus.board_passenger(cash2):
    print(f"Boarded passenger with ${cash2} cash.")
else:
    print(f"Not enough cash to board with ${cash2}.")

bus.display_stats()