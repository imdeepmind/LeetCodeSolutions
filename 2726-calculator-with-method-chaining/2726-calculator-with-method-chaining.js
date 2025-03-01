class Calculator {
    
    /** 
     * @param {number} value
     */
    constructor(value) {
        this.val = value;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    add(value){
        return new Calculator(this.val + value);
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    subtract(value){
        return new Calculator(this.val - value);
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */  
    multiply(value) {
        return new Calculator(this.val * value);
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    divide(value) {
        if (value === 0) throw new Error("Division by zero is not allowed")
        return new Calculator(this.val / value);
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    power(value) {
        return new Calculator(Math.pow(this.val, value));
    }
    
    /** 
     * @return {number}
     */
    getResult() {
        return this.val;
    }
}