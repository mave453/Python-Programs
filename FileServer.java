fileclient.java
import.io.client server
import.io.output
import io.java.in
import.io.java.net
import java.io.*;
import java.net.*;

public class FileServer {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(5000);
        System.out.println("Server started. Waiting for client...");

        Socket socket = serverSocket.accept();
        System.out.println("Client connected.");

        // Read file name
        DataInputStream dis = new DataInputStream(socket.getInputStream());
        String fileName = dis.readUTF();
        System.out.println("Receiving file: " + fileName);

        // Save received file
        FileOutputStream fos = new FileOutputStream("received_" + fileName);
        byte[] buffer = new byte[4096];
        int bytesRead;
        while ((bytesRead = dis.read(buffer)) != -1) {
            fos.write(buffer, 0, bytesRead);
        }

        System.out.println("File received successfully!");
        fos.close();
        dis.close();
        socket.close();
        serverSocket.close();
    }
