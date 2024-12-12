import React, { useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { useNavigation } from '@react-navigation/native';

export default function GroupOrderScreen() {
  const navigation = useNavigation();
  const [statusMessage, setStatusMessage] = useState<string | null>(null); 
  const handleCreateGroup = () => {
    setStatusMessage("Group created! Code: A15S25F06H22");
  };
  const handleJoinGroup = () => {
    setStatusMessage("Joined the group!"); 
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Group Orders</Text>
      <Text style={styles.description}>
        Manage your group orders here. Create a new group or join an existing one to simplify your grocery shopping.
      </Text>
      <TouchableOpacity style={styles.button} onPress={handleCreateGroup}>
        <Text style={styles.buttonText}>Create a Group</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button} onPress={handleJoinGroup}>
        <Text style={styles.buttonText}>Join a Group</Text>
      </TouchableOpacity>
      <TouchableOpacity
        style={styles.startGroupOrder}
        onPress={() => navigation.navigate('marketplace' as never)} >
        <Text style={styles.buttonText}>Start Group Order</Text>
      </TouchableOpacity>
      {statusMessage && <Text style={styles.statusText}>{statusMessage}</Text>}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
    backgroundColor: 'white',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 16,
    color: 'black',
  },
  description: {
    fontSize: 16,
    color: 'grey',
    textAlign: 'center',
    marginBottom: 32,
  },
  button: {
    backgroundColor: '#1d3d47',
    padding: 10,
    borderRadius: 5,
    marginBottom: 10,
  },
  startGroupOrder: {
    backgroundColor: 'orange',
    padding: 10,
    borderRadius: 5,
    marginBottom: 10,
  },
  buttonText: {
    color: 'white',
    fontSize: 14,
    textAlign: 'center',
  },
  statusText: {
    fontSize: 14,
    color: 'black',
    marginTop: 20,
    textAlign: 'center',
  },
});
