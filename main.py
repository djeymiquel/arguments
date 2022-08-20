# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, msg='Hello, <name>!'):
   return msg.replace('<name>', name)

def force(mass, body= 'earth'):
    planet_gravity = {
        'sun' : 274,
        'jupiter' : 24.92,
        'neptune' : 11.15,
        'saturn' : 10.44,
        'earth' : 9.798,
        'uranus' : 8.87,
        'venus' : 8.87,
        'mars' : 3.71,
        'mercury' : 3.7,
        'moon' : 1.62,
        'pluto' : 0.58    
    }
    result = round((mass * planet_gravity[body]))
    return result

def pull(m1,m2,d):
    G = 6.674 * 10 ** -11
   
    return G * ((m1 * m2) / d ** 2)

if __name__ == '__main__':
        
    print(greet('Djey'))
    print(greet('Djey', "what's up, '<name>"))
    print(force(0.1, 'sun'))
    print(pull(800,1500,3)) 