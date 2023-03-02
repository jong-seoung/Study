# import travel.Thailand

# trip_to = travel.Thailand.ThailandPackage()
# trip_to.detail()


# from travel.Thailand import ThailandPackage

# trip_to = travel.Thailand.ThailandPackage()
# trip_to.detail()

# from travel import vietnam

# trip_to = travel.vietnam.vietnamPackage()
# trip_to.detail()

from travel import *
trip_to = vietnam.vietnamPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(Thailand)) #파일 위치 확인