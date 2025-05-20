'''
@Copyright (C): 2010-2021, Shenzhen Yahboom Tech  
@Author: ZiDan  
@Date: 2021-08-26    
@LastEditors: ZiDan    
@LastEditTime: 2021-08-26 
'''
import Adafruit_GPIO as GPIO

class BatteryLevel(object):

    def get_i2c_device(self,address, i2c, i2c_bus):
        if i2c is not None:
            return i2c.get_i2c_device(address)
        else:
            import Adafruit_GPIO.I2C as I2C
            if i2c_bus is None:
                return I2C.get_i2c_device(address)
            else:
                return I2C.get_i2c_device(address, busnum=i2c_bus)
        
    def __init__(self):
        # Create I2C device.
        #"""Initialize the RGB."""
        # Setup I2C interface for the device.
#         if i2c is None:
#             import Adafruit_GPIO.I2C as I2C
#             i2c = I2C
        self._device = self.get_i2c_device(0x1b, None, 1)
    
    def Update(self):
        AD_value = self._device.readList(0x00,2)
        Battery_vol = ((AD_value[0] << 8) + AD_value[1]) * 13.3 / 1023.0
        print(Battery_vol)
        #充电电量判断
        #Charging quantity judgment
        if Battery_vol >= 12:
            return 'Battery_High'
        elif Battery_vol >= 11.1:
            return 'Battery_Medium'
        elif Battery_vol >= 10.05:
            return 'Battery_Low'
        #放电电量判断
        #Discharge quantity judgment
        if Battery_vol <= 9.9:
            return 'Battery_Empty'
        elif Battery_vol <= 10.95:
            return 'Battery_Low'
        elif Battery_vol <= 11.85:
            return 'Battery_Medium'