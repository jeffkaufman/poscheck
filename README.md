Prohibit Positional Arguments
-----------------------------

If you have a function that you want to always be called with keyword arguments, you
can make them mandatory with `poscheck`:

    @poscheck
    def always_keyword(data, model)
      ...

Then calls like `always_keyword(data=x, model=y)` will succeed, but calls like
`always_keyword(x, y)` will get a `PositionalArgumentsError`:

    Traceback (most recent call last):
      File "tests.py", line 55, in <module>
        start()
      File "tests.py", line 32, in start
        checked(1, 2)
      File "poscheck/poscheck.py", line 10, in checked_f
        raise PositionalArgumentsError(f)
    poscheck.PositionalArgumentsError: checked takes only keyword arguments
