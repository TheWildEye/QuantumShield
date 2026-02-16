# KEMTLS Test Dashboard

A comprehensive web-based dashboard for testing and monitoring KEMTLS (post-quantum TLS) implementation.

## Features

### 1. Test Cases Dashboard
- **Protocol Tests**: Validate complete KEMTLS handshake flow
- **Security Tests**: Verify cryptographic operations (signature verification, KEM)
- **Performance Tests**: Measure handshake timing and throughput
- **Failure Injection Tests**: Test error handling (invalid signatures, corrupt ciphertext, etc.)

### 2. Real-time System Monitor
- **Server Status**: Uptime, active sessions, total handshakes
- **Performance Metrics**: Handshakes/sec, latency, throughput
- **Resource Usage**: CPU, memory, network monitoring
- **Active Sessions**: Live view of ongoing KEMTLS sessions
- **Real-time Charts**: Visual representation of metrics over time

### 3. Test Results
- Detailed test execution results
- Performance metrics for each test
- Security validation results
- Error logs and debugging information

### 4. Live Logs
- Real-time event streaming
- Phase-by-phase handshake logging
- Filterable by log level and source
- Auto-scrolling capability

## Installation

1. Install Python dependencies:
```bash
cd web_demo
pip install -r requirements.txt
```

2. Run the dashboard server:
```bash
python app_enhanced.py
```

3. Open your browser and navigate to:
```
http://localhost:9000/dashboard
```

## Usage

### Running Tests

1. **Create a New Test**:
   - Click "New Test" button
   - Fill in test details (name, type, description)
   - Configure crypto algorithms (Kyber768, Dilithium3, etc.)
   - Select failure mode (for failure injection tests)
   - Click "Create Test"

2. **Run Individual Test**:
   - Click the "Run" button on any test card
   - Watch real-time progress in the logs
   - View results when complete

3. **Run All Tests**:
   - Click "Run All Tests" in the header
   - All pending tests will execute sequentially

### Monitoring System

1. Navigate to the "System Monitor" tab
2. View real-time metrics:
   - Server status and uptime
   - Active KEMTLS sessions
   - Performance graphs
   - Resource utilization

### Viewing Results

1. Navigate to the "Results" tab
2. See all completed test results
3. Click on individual tests for detailed breakdown
4. Export results (coming soon)

### Live Logs

1. Navigate to the "Live Logs" tab
2. See real-time event stream
3. Filter by log level (DEBUG, INFO, WARN, ERROR)
4. Toggle auto-scroll on/off
5. Clear logs as needed

## Test Types

### Protocol Tests
- Basic KEMTLS Handshake
- OIDC over KEMTLS
- Multi-session tests

### Security Tests
- Signature Verification
- KEM Encapsulation/Decapsulation
- Shared Secret Validation
- Forward Secrecy

### Performance Tests
- Handshake Performance
- Throughput Measurement
- Latency Testing
- Resource Usage

### Failure Injection Tests
- Invalid Signature
- Corrupt Ciphertext
- Network Timeout
- Wrong Keys
- Replay Attacks

## Configuration

Tests can be configured with:
- **KEM Algorithm**: Kyber512, Kyber768, Kyber1024
- **Signature Algorithm**: Dilithium2, Dilithium3, Dilithium5
- **Symmetric Cipher**: AES-128-GCM, AES-256-GCM, ChaCha20-Poly1305
- **Network Parameters**: Latency, packet loss, bandwidth
- **Failure Modes**: Various error conditions

## WebSocket API

The dashboard uses WebSocket for real-time updates:

### Client → Server Messages
```json
{
  "type": "subscribe_test",
  "data": { "testId": "test-123" }
}
```

### Server → Client Messages
```json
{
  "type": "test_event",
  "data": {
    "testId": "test-123",
    "phase": "server_hello",
    "timestamp": "2024-02-08T10:30:00Z",
    "message": "Server sends public keys"
  }
}
```

## REST API

### Endpoints

**Tests**
- `GET /api/tests` - List all tests
- `POST /api/tests` - Create new test
- `GET /api/tests/:id` - Get test details
- `POST /api/tests/:id/run` - Run test

**System**
- `GET /api/system/state` - Get system state
- `GET /api/system/metrics` - Get metrics

## Architecture

```
web_demo/
├── app_enhanced.py          # Main Flask application with WebSocket
├── templates/
│   ├── dashboard.html       # Main dashboard UI
│   └── login.html          # Original demo login
├── static/
│   ├── dashboard.css       # Dashboard styles
│   ├── dashboard.js        # Dashboard logic & WebSocket
│   ├── demo.css           # Original demo styles
│   └── demo.js            # Original demo logic
└── requirements.txt        # Python dependencies
```

## Integration with KEMTLS

The dashboard integrates with your existing KEMTLS implementation:

1. **Test Execution**: Calls KEMTLS protocol implementation
2. **Event Streaming**: Captures handshake phases in real-time
3. **Metrics Collection**: Measures crypto operation performance
4. **Error Handling**: Tests failure scenarios

## Development

### Adding New Tests

Add new test definitions in `dashboard.js`:

```javascript
{
    id: 'test-custom',
    type: 'protocol',
    name: 'Custom Test',
    description: 'Description here',
    status: 'pending',
    config: {
        kemAlgorithm: 'Kyber768',
        signatureAlgorithm: 'Dilithium3'
    }
}
```

### Customizing UI

- Edit `dashboard.css` for styling
- Modify `dashboard.html` for layout
- Update `dashboard.js` for functionality

## Troubleshooting

**WebSocket not connecting**:
- Check if port 9000 is available
- Ensure firewall allows WebSocket connections
- Try using REST API fallback

**Tests not running**:
- Verify KEMTLS backend is accessible
- Check network configuration
- Review logs for error messages

**Charts not displaying**:
- Ensure Chart.js is loaded
- Check browser console for errors
- Verify data is being received

## Future Enhancements

- [ ] Export test results to PDF/CSV
- [ ] Historical data analysis
- [ ] Comparison with TLS performance
- [ ] Custom test scripting
- [ ] Multi-user support
- [ ] Test scheduling
- [ ] Email notifications
- [ ] Integration with CI/CD

## License

Same as the main KEMTLS implementation.

## Support

For issues or questions, please refer to the main project documentation.
