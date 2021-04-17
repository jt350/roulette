#! python3
import random

while True:
    spin = input('Press enter to spin the wheel.')
    rwheel={
    '00':['Green'],
    '0':['Green'],
    '1':['Red','1st 12','1st Column','1st 18','Odd'],
    '2':['Black','1st 12','2nd Column','1st 18','Even'],
    '3':['Red','1st 12','3rd Column','1st 18','Odd'],
    '4':['Black','1st 12','1st Column','1st 18','Even'],
    '5':['Red','1st 12','2nd Column','1st 18','Odd'],
    '6':['Black','1st 12','3rd Column','1st 18','Even'],
    '7':['Red','1st 12','1st Column','1st 18','Odd'],
    '8':['Black','1st 12','2nd Column','1st 18','Even'],
    '9':['Red','1st 12','3rd Column','1st 18','Odd'],
    '10':['Black','1st 12','1st Column','1st 18','Even'],
    '11':['Black','1st 12','2nd Column','1st 18','Odd'],
    '12':['Red','1st 12','3rd Column','1st 18','Even'],
    '13':['Black','2nd 12','1st Column','1st 18','Odd'],
    '14':['Red','2nd 12','2nd Column','1st 18','Even'],
    '15':['Black','2nd 12','3rd Column','1st 18','Odd'],
    '16':['Red','2nd 12','1st Column','1st 18','Even'],
    '17':['Black','2nd 12','2nd Column','1st 18','Odd'],
    '18':['Red','2nd 12','3rd Column','1st 18','Even'],
    '19':['Red','2nd 12','1st Column','2nd 18','Odd'],
    '20':['Black','2nd 12','2nd Column','2nd 18','Even'],
    '21':['Red','2nd 12','3rd Column','2nd 18','Odd'],
    '22':['Black','2nd 12','1st Column','2nd 18','Even'],
    '23':['Red','2nd 12','2nd Column','2nd 18','Odd'],
    '24':['Black','2nd 12','3rd Column','2nd 18','Even'],
    '25':['Red','3rd 12','1st Column','2nd 18','Odd'],
    '26':['Black','3rd 12','2nd Column','2nd 18','Even'],
    '27':['Red','3rd 12','3rd Column','2nd 18','Odd'],
    '28':['Black','3rd 12','1st Column','2nd 18','Even'],
    '29':['Black','3rd 12','2nd Column','2nd 18','Odd'],
    '30':['Red','3rd 12','3rd Column','2nd 18','Even'],
    '31':['Black','3rd 12','1st Column','2nd 18','Odd'],
    '32':['Red','3rd 12','2nd Column','2nd 18','Even'],
    '33':['Black','3rd 12','3rd Column','2nd 18','Odd'],
    '34':['Red','3rd 12','1st Column','2nd 18','Even'],
    '35':['Black','3rd 12','2nd Column','2nd 18','Odd'],
    '36':['Red','3rd 12','3rd Column','2nd 18','Even']
    }

    wnum = random.choice(list(rwheel))

    print ('The winning nuber is ', wnum, '\n- Additional PayOuts: \n', rwheel[wnum], '\n \n')