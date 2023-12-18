wall_height = int(input('What is the wall height? '))
wall_width = int(input('What is the wall width? '))
coverage = int(input('What is the coverage per can? '))


def number_of_cans(wall_height, wall_width, coverage):
    total_cans = round((wall_height * wall_width) / coverage)
    
    print(f'You need {str(total_cans)} of cans of paint')


number_of_cans(wall_height, wall_width, coverage)