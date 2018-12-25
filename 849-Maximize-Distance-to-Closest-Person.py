def maxDistToClosest(seats):
    list_empty_seats = []
    count_empty_seats = 0

    for i in range(len(seats)):
        if i < (len(seats)-1) and seats[i] == seats[i+1] == 0:
            count_empty_seats += 1
        else:
            if count_empty_seats >= 0:
                list_empty_seats.append(count_empty_seats+1)
                count_empty_seats = 0

    return max(list_empty_seats)

seats = [0,1,0,1,0,0,1]
print maxDistToClosest(seats)