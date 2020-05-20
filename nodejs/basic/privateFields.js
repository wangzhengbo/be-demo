class Foo {
  #b = 15

  get() {
    return this.#b
  }

  increment() {
    ++this.#b
  }
}

const obj = new Foo()
obj.increment()
console.log('value', obj.get())

console.log("obj['#b']", obj['#b']) // undefined
console.log("obj.hasOwnProperty('#b')", obj.hasOwnProperty('#b')) // false

// SyntaxError: Undefined private field #b: must be declared in an enclosing class
// obj.#b

console.log('Object.keys(obj)', Object.keys(obj)) // []
console.log('Object.getOwnPropertyDescriptors(obj)', Object.getOwnPropertyDescriptors(obj)) // {}