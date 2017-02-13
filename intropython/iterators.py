days = ['Monday','Tuesday', 'Wednesday']
fruits = ['banana','orange','peach']
drinks = ['coffee','tea','beer']
desserts = ['tiramisu', 'ice cream','pie','pudding']

for day,fruit,drink,dessert in \
    zip(days,fruits,drinks,desserts):
    print(day,": drink",drink, "-eat",fruit,"-enjoy", dessert)


combine = list(zip(days,desserts))

print(combine)

combine = dict(zip(days,desserts))

print(combine)
