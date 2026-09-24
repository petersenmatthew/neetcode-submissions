class Solution:
    def time_to_end(self, target, position, speed):
        return (target - position) / speed

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position, speed), reverse=True)
        stack = [] # store tte's
        for car in pos_speed:
            car_position = car[0]
            car_speed = car[1]
        
            car_tte = self.time_to_end(target, car_position, car_speed)

            if len(stack) != 0:
                top_tte = stack[-1]
                if car_tte <= top_tte:
                    pass
                else:
                    stack.append(car_tte)
            else:
                stack.append(car_tte)
        return len(stack)
                

  
