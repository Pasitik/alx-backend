const redis = require('redis');

// Create a Redis client
const client = redis.createClient({
  host: '127.0.0.1',
  port: 6379,
});

// Handle connection and error events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error('Redis client not connected to the server: ', err);
});
client.quit()
