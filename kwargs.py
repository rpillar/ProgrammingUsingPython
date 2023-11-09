# you can (and maybe you want to) pass arguments to a function by keyword only
# or have a scenario where you may want to mix positional and keyword  args
# but want the user to always supply formatted keyword args

def func1(arg1, arg2, arg3="foo"):
    print(f"My args are {arg1}, {arg2} and {arg3}")

func1("Hello", "World") # arg3 in this case 'defaults' to "foo"
func1("Hello", "World", "again") # note you can supply a valaue to arg3 as a positional arg

# to 'force' the user to supply properly formatted keyword/value args 
# separate the positional and keyword args with a single asterisk (*)

def func2(arg1, *, name="Joe"):
    print(f"My name is {name}")

# in this case we get an error :- 
# TypeError: func2() takes 1 positional argument but 2 were given
#func2(1,"Richard") 

# supply the keyword arg
func2(1, name="Richard")