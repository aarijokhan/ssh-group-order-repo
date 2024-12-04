import React, { useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { NavigationProp, useNavigation } from '@react-navigation/native';

type RootStackParamList = { 
    'marketplace': undefined
} 
export default function GroupOrderScreen() {
    const navigation = useNavigation<NavigationProp<RootStackParamList>>();
    const [statusMessage, setStatusMessage] = useState<string| null>(null);
    const handleCreateGroup = () => {
        setStatusMessage ("You have successfully created a group!\n The code to join your group is A15S25F06H22")
    }

    const handleJoinGroup = () => {
        setStatusMessage ("You have successfully joined the group!")
    }

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
      <TouchableOpacity style={styles.startGroupOrder} onPress={() => navigation.navigate('marketplace')}>
        <Text style={styles.buttonText}>Start Group Order</Text>
      </TouchableOpacity>
      {statusMessage && ( <Text style={styles.statusText}>{statusMessage}</Text> )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
    backgroundColor: '#f9f9f9',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 16,
    color: '#1d3d47',
  },
  description: {
    fontSize: 16,
    color: '#666666',
    textAlign: 'center',
    marginBottom: 32,
  },
  button: {
    backgroundColor: '#1d3d47',
    borderRadius: 8,
    paddingVertical: 12,
    paddingHorizontal: 24,
    marginBottom: 16,
  },
  buttonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  statusText: {
    fontSize: 18,
    color: '#1d3d47',
    textAlign: 'center',
    marginTop: 24,
  },
  startGroupOrder: {
    backgroundColor: '#007AFF',
    borderRadius: 8,
    paddingVertical: 12,
    paddingHorizontal: 24,
    marginBottom: 16,
  }
});
