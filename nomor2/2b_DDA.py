# Moch Yogi Firmansyah
# 20051397044
# 2020B

import matplotlib.pyplot as plt


def DDALine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
   
    # calculate steps required for generating pixels 
   
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
         
    #calculate increment in x & y for each steps
    Xinc = float(dx / steps)
    Yinc = float(dy / steps)
    
        
    for i in range(0, int(steps + 1)):
		 # Draw pixels
        plt.plot(int(x1), int(y1), color)
        x1 += Xinc
        y1 += Yinc
    plt.show()


def main():
    x = int(7)
    y = int(-1)
    xEnd = int(-4)
    yEnd = int(-6)
    color = "r."
    DDALine(x, y, xEnd, yEnd, color)


if __name__ == '__main__':
    main()
