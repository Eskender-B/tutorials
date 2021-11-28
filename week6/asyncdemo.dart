import 'dart:convert';
import 'dart:io';

Future<bool> requestLogin(String _un, String _p) async {
  if (_un == "" || _p == "") {
    return false;
  } else {
    HttpClient client = HttpClient();
    HttpClientRequest req = await client.getUrl(
        Uri.parse("http://localhost:5000/login?username=$_un&password=$_p"));
    HttpClientResponse resp = await req.close();
    String strresp = await utf8.decodeStream(resp);
    print(strresp);
    return true;
  }
}

void testnetio() async {
  HttpClient client = HttpClient();
  HttpClientRequest req = await client.getUrl(Uri.parse("https://google.com"));
  HttpClientResponse resp = await req.close();
  String strresp = await utf8.decodeStream(resp);
  print(strresp);
}

void main() async {
  requestLogin("dagim", "thepass");
}
