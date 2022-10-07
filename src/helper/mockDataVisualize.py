from random import randrange
from typing import Dict

#I assume that we can a dict in form of:
# key = sentence
# value = how important it is, in my example it will be 4 most important, 0 least important
def mockData() -> Dict[str,int]:
    lorem_ipsum = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in ligula diam. Aliquam erat volutpat. Aliquam eget tellus egestas, vehicula nunc sed, vulputate tellus. Aliquam et tortor sed dui porta porta eget vel erat. Curabitur non massa tellus. Phasellus ut malesuada lacus. Nullam et eros nec lectus facilisis convallis. Nam tincidunt quis turpis vitae accumsan. Aenean lectus arcu, scelerisque in elit sit amet, molestie fringilla mauris.

Maecenas blandit, neque et volutpat tristique, enim ex pharetra urna, id efficitur orci sapien at risus. Curabitur neque odio, lacinia vitae leo et, convallis maximus sem. Sed facilisis gravida elit, et placerat purus pellentesque vel. Ut quis mattis dolor, id consequat odio. Donec fringilla orci eu justo pharetra, ac consectetur lorem ultricies. Phasellus in hendrerit ligula. Maecenas congue ullamcorper urna, id euismod elit pulvinar ut. Morbi vehicula porttitor eros ullamcorper convallis. Pellentesque porttitor dapibus quam, et ultricies enim sollicitudin ut. Curabitur ornare sodales sollicitudin. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nullam dictum urna vitae lorem auctor efficitur.

Praesent suscipit in elit vel elementum. Vestibulum iaculis hendrerit tincidunt. Aenean mauris tellus, sagittis sit amet ligula et, lobortis posuere felis. Maecenas malesuada quis nibh vitae scelerisque. Sed consequat justo vel orci posuere elementum. In consectetur mauris vitae sapien interdum porta. Nunc ut condimentum diam, nec tristique nulla.

Mauris mattis porta lobortis. Suspendisse sem tortor, lobortis viverra est quis, ullamcorper dignissim ex. Vivamus eu enim eleifend, aliquet nunc quis, faucibus elit. Proin ullamcorper lectus dolor, at aliquet eros tempor in. Proin ut scelerisque libero, et sodales diam. Duis quis neque efficitur, accumsan massa at, mattis nulla. Nam id augue at ex elementum tincidunt sit amet eget ipsum. Vestibulum iaculis, ipsum eu tempor bibendum, lorem turpis posuere dolor, bibendum auctor lectus enim sed sapien. Phasellus porta sem viverra, gravida mi id, consectetur lectus. Curabitur tempus hendrerit elementum. Phasellus viverra dignissim ipsum et luctus. Sed sed ornare odio. Sed quis ultricies purus, a porta odio. Aenean consequat urna at velit iaculis, ac blandit erat fringilla. Nulla nec convallis metus. Phasellus porta, nisl id molestie condimentum, orci lectus ultrices libero, aliquam fringilla augue urna id dui.

Duis posuere mauris non ipsum porttitor, ut ultricies nulla auctor. Curabitur eleifend augue dolor, ac porta est scelerisque vel. Morbi vestibulum sodales feugiat. Phasellus efficitur diam quis diam tempor gravida. Mauris ornare venenatis ipsum, in interdum tellus efficitur sit amet. Nunc eu nisi dictum, ultricies lectus a, imperdiet ex. Pellentesque eget mi mattis, tempus est sit amet, placerat ligula. Sed consectetur at neque molestie aliquam. Pellentesque mollis scelerisque lorem, in aliquet quam interdum eu. Vivamus auctor dapibus sagittis. In enim arcu, pellentesque eget sem vel, semper eleifend velit. Cras id lobortis tellus. Nam sed purus fermentum nisl tincidunt dignissim. Mauris hendrerit enim vel justo lacinia, lacinia maximus lacus faucibus.'''
    split_by_dot = lorem_ipsum.split(".")
    ranking_dict = {}
    for sentence in split_by_dot:
        ranking_dict[sentence] = randrange(5)  
    return ranking_dict