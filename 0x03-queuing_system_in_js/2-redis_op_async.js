const redis = require('redis');
const {promisify} = require('util')


// Create a Redis client
const client = redis.createClient({
  host: '127.0.0.1',
  port: 6379,
});

const promisifiedGet = promisify(client.get).bind(client);
// Handle connection and error events
client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
});

client.on('error', (err) => {
  console.error('Redis client not connected to the server: ', err);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
	if (!err) {
	  redis.print(`Reply: ${reply}`);
	}
  });
}

async function displaySchoolValue(value) {
  const promisifiedGet = promisify(client.get).bind(client);
  try {
	const val = await promisifiedGet(value)
	console.log(val)
  } catch (error) {
	console.error('Error getting value:', error);
  } 
}
//client.quit();
