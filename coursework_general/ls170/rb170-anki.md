## What is the Internet?
The Internet is a vast network of networks comprising both the physical infrastructure (devices, routers, cables) and the protocols enabling it to function.

## What is the difference between the Internet and the World Wide Web?
The Internet is the global network infrastructure that connects computers worldwide, while the World Wide Web (WWW) is an application layer service built on top of the Internet that uses HTTP to transfer hypertext documents.

## What is a protocol in networking?
A protocol is a set of rules that governs how data is transmitted between devices on a network. It defines the format, timing, sequencing, and error checking methods used in data communication.

## What are the layers of the TCP/IP model?
The TCP/IP model has four layers:
1. Application Layer (HTTP, DNS, SMTP)
2. Transport Layer (TCP, UDP)
3. Internet Layer (IP, ICMP)
4. Link Layer (Ethernet, Wi-Fi)

## What is the role of the Application Layer?
The Application Layer provides protocols that directly serve end-user applications. It includes protocols like HTTP for web browsing, SMTP for email, FTP for file transfers, and DNS for domain name resolution.

## What is the role of the Transport Layer?
The Transport Layer provides end-to-end communication services for applications. It handles data segmentation, transmission reliability (TCP), connection management, flow control, and multiplexing through ports.

## What is the role of the Internet Layer?
The Internet Layer handles logical addressing (IP addresses) and routing of packets across networks. Its primary protocol is IP (Internet Protocol), which provides addressing and routing capabilities.

## What is the role of the Link Layer?
The Link Layer deals with the physical transmission of data over the network medium. It includes protocols for physical addressing (MAC), media access control, and error detection at the hardware level.

## What is encapsulation in networking?
Encapsulation is the process where each protocol layer adds its header information to the data it receives from the layer above before passing it to the layer below. This creates a nested structure of headers around the original data.

## What is the difference between TCP and UDP?
TCP (Transmission Control Protocol) is connection-oriented, reliable, maintains message order, and has built-in error checking and flow control. UDP (User Datagram Protocol) is connectionless, unreliable, has no guaranteed order, but has less overhead and is faster for applications where some data loss is acceptable.

## What is the three-way handshake in TCP?
The TCP three-way handshake is a process to establish a connection:
1. Client sends SYN packet to server
2. Server responds with SYN-ACK
3. Client acknowledges with ACK
This process synchronizes sequence numbers and establishes parameters for the connection before any data is transmitted.

## What is an IP address?
An IP address is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol. It serves two main functions: host/network interface identification and location addressing.

## What is DNS and how does it work?
DNS (Domain Name System) is a hierarchical, distributed database that translates domain names (like example.com) to IP addresses. It works through a process of recursive and iterative queries to root servers, TLD servers, and authoritative name servers to resolve domain names.

## What is HTTP?
HTTP (Hypertext Transfer Protocol) is an application layer protocol that forms the foundation of data communication on the Web. It defines how messages are formatted and transmitted, and how servers and browsers should respond to various commands.

## What is the HTTP request/response cycle?
The HTTP request/response cycle is the process where:
1. A client sends an HTTP request to a server
2. The server processes the request
3. The server returns an HTTP response to the client
4. The client processes the response (e.g., renders a webpage)

## What are the components of an HTTP request?
An HTTP request consists of:
- Request line (method, path, HTTP version)
- Headers (metadata about the request)
- Empty line
- Message body (optional, contains data for POST/PUT requests)

## What are the components of an HTTP response?
An HTTP response consists of:
- Status line (HTTP version, status code, reason phrase)
- Headers (metadata about the response)
- Empty line
- Message body (contains the requested resource)

## What are common HTTP methods?
Common HTTP methods include:
- GET: Request data from a server
- POST: Submit data to be processed
- PUT: Update an existing resource
- DELETE: Remove a resource
- HEAD: Same as GET but without the response body
- OPTIONS: Request permitted communication options
- PATCH: Apply partial modifications

## What are HTTP status codes?
HTTP status codes are three-digit numbers returned in HTTP responses that indicate the outcome of the request:
- 1xx: Informational
- 2xx: Success (e.g., 200 OK)
- 3xx: Redirection (e.g., 301 Moved Permanently)
- 4xx: Client Error (e.g., 404 Not Found)
- 5xx: Server Error (e.g., 500 Internal Server Error)

## What is HTTPS and how does it differ from HTTP?
HTTPS (HTTP Secure) is HTTP over TLS/SSL encryption. It differs from HTTP by providing:
- Encrypted communication that prevents eavesdropping
- Authentication of the website with certificates
- Data integrity verification to prevent tampering
HTTPS uses port 443 by default, while HTTP uses port 80.

## What is TLS/SSL?
TLS (Transport Layer Security) and its predecessor SSL (Secure Sockets Layer) are cryptographic protocols that provide communication security over a network. They use certificates, encryption, and handshakes to establish secure connections.

## What is a URL and what are its components?
A URL (Uniform Resource Locator) is an address that specifies the location of a resource on the internet. Its components include:
- Scheme (e.g., http, https)
- Host (domain name or IP address)
- Port (optional, defaults based on scheme)
- Path (resource location on the server)
- Query string (additional parameters after ?)
- Fragment (reference within the resource after #)
