def get_data_fig(*args, **kwargs):
    perim = sum(args)
    options = ('tp', 'color', 'closed','width')
    res_values = (kwargs[key] for key in options if key in kwargs)

    return perim, *res_values


print(get_data_fig(1,2,3, tp=True, color=45))