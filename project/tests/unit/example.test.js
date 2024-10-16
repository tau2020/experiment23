const exampleFunction = require('../src/example');

describe('exampleFunction', () => {
  it('should return the correct value for input 1', () => {
    expect(exampleFunction(1)).toBe('Expected Output 1');
  });

  it('should return the correct value for input 2', () => {
    expect(exampleFunction(2)).toBe('Expected Output 2');
  });

  it('should throw an error for invalid input', () => {
    expect(() => exampleFunction(null)).toThrow('Invalid input');
  });
});