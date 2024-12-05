const redis = require('redis');
const {promisify} = require('util')

// Create a Redis client
const client = redis.createClient({
  host: '127.0.0.1',
  port: 6379,
});


client.on('error', (err) => {
  console.error('Redis connection error:', err);
});

function main() {
  client.HSET('HolbertonSchools', 'Portland', '50', redis.print)
  client.HSET('HolbertonSchools', 'Seattle', '80', redis.print)
  client.HSET('HolbertonSchools', 'New York', '20', redis.print)
  client.HSET('HolbertonSchools', 'Bogota', '20', redis.print)
  client.HSET('HolbertonSchools', 'Cali', '40', redis.print)
  client.HSET('HolbertonSchools', 'Paris', '2', redis.print)
  client.HGETALL('HolbertonSchools', (err, val) => {
    if (err) {
	console.log(err)
    }  
     console.log(val)
  })
}


// Handle connection and error events
client.on('connect', () => {
  console.log('Connected to Redis');
  main()
});

