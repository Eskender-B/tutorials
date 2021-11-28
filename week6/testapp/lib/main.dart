import 'package:flutter/material.dart';

void main() => runApp(OurApp());

class OurApp extends StatelessWidget {
  const OurApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    String username = "";
    String password = "";
    return MaterialApp(
      home: Builder(
        builder: (BuildContext context) => Scaffold(
          body: SafeArea(
            child: Column(
              children: [
                SizedBox(
                  height: 50,
                ),
                Image.asset(
                  "assets/images/mylogo.png",
                  width: 220,
                ),
                Container(
                  padding: EdgeInsets.only(top: 30, left: 50, right: 50),
                  child: Column(
                    children: [
                      TextField(
                        onChanged: (_username) {
                          username = _username;
                        },
                        decoration: const InputDecoration(
                          hintText: 'Enter your Username',
                          labelText: 'Username',
                        ),
                      ),
                      TextField(
                        onChanged: (_password) {
                          password = _password;
                        },
                        decoration: const InputDecoration(
                          hintText: 'Enter your Password',
                          labelText: 'Password',
                        ),
                      ),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.end,
                        children: [
                          ElevatedButton(
                            onPressed: () {
                              showDialog(
                                context: context,
                                builder: (BuildContext context) => AlertDialog(
                                  title: const Text("Check input"),
                                  content:
                                      Text("Input: $username and $password"),
                                  actions: [
                                    TextButton(
                                      onPressed: () {
                                        Navigator.of(context).pop();
                                      },
                                      child: const Text("Cancel"),
                                    ),
                                    TextButton(
                                      onPressed: () {},
                                      child: const Text("Ok"),
                                    ),
                                  ],
                                ),
                              );
                            },
                            child: const Text("Submit"),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
