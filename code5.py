def eucledian(x1,y1,x2,y2):
    x_temp=(x2-x1)**2
    y_temp=(y2-y1)**2
    distance=(x_temp + y_temp)**.5
    return distance


print(eucledian(23.43,43.34,35.33,47.82))