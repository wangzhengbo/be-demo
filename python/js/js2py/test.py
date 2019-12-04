import js2py

js2py.eval_js('console.log( "Hello World!" )')

add = js2py.eval_js('function add(a, b) {return a + b}')
print(add(1, 2) + 3)

print(js2py.eval_js('(function add(a, b) {return a + b})(2, 3)'))