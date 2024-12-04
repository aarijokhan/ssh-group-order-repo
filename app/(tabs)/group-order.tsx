import React, { useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';

export default function GroupOrderScreen() {
  const [groupStatus, setGroupStatus] = useState('');

  const handleCreateGroup = () => {
    setGroupStatus('You have successfully created a group!\n The code to join the group is A15S25F06H22');
  };

  const handleJoinGroup = () => {
    setGroupStatus('You have successfully joined a group!');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Group Orders</Text>
      <Text style={styles.description}>
        Manage your group orders here. Create a new group or join an existing one to simplify your grocery shopping.
      </Text>

      {/* Create Group Button */}
      <TouchableOpacity style={styles.button} onPress={handleCreateGroup}>
        <Text style={styles.buttonText}>Create a Group</Text>
      </TouchableOpacity>

      {/* Join Group Button */}
      <TouchableOpacity style={styles.button} onPress={handleJoinGroup}>
        <Text style={styles.buttonText}>Join a Group</Text>
      </TouchableOpacity>

      {/* Display group status */}
      {groupStatus ? (
        <Text style={styles.statusText}>{groupStatus}</Text>
      ) : null}
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
});
