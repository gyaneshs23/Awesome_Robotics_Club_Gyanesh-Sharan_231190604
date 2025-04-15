# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 15:15:23 2025

@author: GYANESH SHARAN
"""

import math
L1 = 5.0   
L2 = 10.0  
L3 = 15.0  
def transform (x, y, z):
    return x, y, z  
def inverse_kinematics(x, y, z):
        α = math.atan2(y, x)  
        x1 = math.sqrt(x**2 + y**2) - L1 
        z1 = z  
        D = math.sqrt(x1**2 + z1**2)
        S=  math.sqrt(x**2 + y**2 + z**2)

        if S> (L1+L2+L3):
            return "Unreachable position"

        cosϒ= (D**2 - L2**2 - L3**2) / (2 * L2 * L3)
        ϒ= math.acos(cosϒ) 
        θ = math.atan2(z1, x1)
          
        Φ = math.acos((L2**2 + D**2 - L3**2) / (2 * L2 * D))
        β = θ- Φ 
        α_d= math.degrees(α)
        β_d= math.degrees(β)
        ϒ_d= math.degrees(ϒ)

        return α_d, β_d, ϒ_d
        
   
def end_effector_pos_user_input():
        x = float(input("Enter end-effector's X position: "))
        y = float(input("Enter end-effector's Y position: "))
        z = float(input("Enter end-effector's Z position: "))
        x, y, z = transform (x, y, z)
        result = inverse_kinematics (x, y, z)

        if isinstance(result, str):
            print(result)
        else:
            α,β,ϒ= result
            print("\nCalculated Joint Angles (in degrees):")
            print(f"Coxa (α) = {α:.2f}°")
            print(f"Femur (β) = {β:.2f}°")
            print(f"Tibia (ϒ) = {ϒ:.2f}°")
end_effector_pos_user_input()
