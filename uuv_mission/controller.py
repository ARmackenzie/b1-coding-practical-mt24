class PDController:
    def __init__(self, kp: float, kd: float):
        self.kp = kp  # Proportional gain
        self.kd = kd  # Derivative gain
        self.previous_error = 0.0  # To store the last error

    def compute(self, setpoint: float, current_value: float) -> float:
        error = setpoint - current_value  # Calculate the error
        derivative = (error - self.previous_error)   # Calculate the derivative
        output = self.kp * error + self.kd * derivative  # PD control formula
        self.previous_error = error  # Store current error for next derivative calculation
        return output