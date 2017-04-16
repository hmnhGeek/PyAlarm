print 'PyAlarm'

import datetime as t
import winsound as w


def check(a):

    if len(a) == 1:
        a = '0'+a
        return a
    else:
        return a

def alarm():
    print
    #print 'Every data must be in 2 digits.'
    #print
    try:
        
        clc = raw_input('What type of clock? (24/12) ')
        if clc == '24':
            
            h = raw_input('Enter hr: ')
            m = raw_input('Enter minutes: ')
            s = raw_input('Enter second: ')
            freq = raw_input('Enter frequency for alarm: ')
            h = check(h)
            m = check(m)
            s = check(s)

            string = h+':'+m+':'+s

        elif clc == '12':

            h = raw_input('Enter hr: ')
            m = raw_input('Enter minutes: ')
            s = raw_input('Enter second: ')
            freq = raw_input('Enter frequency for alarm: ')
            meridian = raw_input('am or pm: ')

            if meridian == 'am':
                h = check(h)
                m = check(m)
                s = check(s)
                string = h+':'+m+':'+s

            elif meridian == 'pm':
                h = check(h)
                m = check(m)
                s = check(s)

                h = str(12+int(h))
                string = h+':'+m+':'+s

        else:
            print 'Invalid clock type!'

        try:
            if freq == '':
                pass
            else:
                
                int(freq)
        except ValueError:
            print 'Please give integer value to frequency.'
            alarm()

        def run():

            if freq =='':
                for i in [1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111]:
                    w.Beep(i, 200)
            else:
                for i in range(2):
                
                    w.Beep(int(freq), 5000)
            alarm()

        while string<>str(t.datetime.now())[11:19]:
            pass
        else:
            run()

    except UnboundLocalError:
        print
        print 'Please specify a type of clock to continue.'
        alarm()
alarm()

    

    
