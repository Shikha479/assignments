
function isPrime(value){
	

	for (let i=2; i<value; i++){
		if(value%i == 0){
			console.log(value+" is not a prime number.")
			break;
		}
	
	}
	return value>1;

	
}
	
console.log(isPrime(7));







