# TXTpresso Example

This example demonstrates a basic usage of the TXTpresso DNS-based communication system. It includes a simple `TimeHandler` that responds to DNS TXT queries with the current server time.

## How It Works

The `TimeHandler` is a custom handler that, when queried, returns the current date and time. This handler is registered to the TXTpresso server under the action 'time'. When the server receives a DNS TXT query for `time.txtpresso`, it invokes the `TimeHandler` and responds with the current time.

## Running the Example

To run this example, follow these steps:

1. **Start the TXTpresso Server**:
   - Navigate to the directory containing `example.py`.
   - Run the script using Python:
     ```
     python example.py
     ```

2. **Query the Server**:
   - Use a DNS query tool like `dig` to query the TXTpresso server. For example:
     ```bash
     dig @localhost -p 53 +short txt time.txtpresso
     ```
   - This command sends a TXT query to the TXTpresso server running on `localhost` at port 53, asking for the current time associated with `time.txtpresso`.

## Expected Output

The server will respond to the query with the current date and time in the format `YYYY-MM-DD HH:MM:SS`. For example, you might see a response like `2024-02-04 15:30:45`.

## Note

- Ensure that no other service is using port 53 on your machine, as the TXTpresso server needs to bind to this port to listen for DNS queries.
- The server runs indefinitely until stopped. To stop the server, use `Ctrl+C` in the terminal where it's running.
