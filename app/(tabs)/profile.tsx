import React from 'react';
import { View, Text, StyleSheet, SafeAreaView, ScrollView, TouchableOpacity } from 'react-native';

export default function ProfileScreen() {
  return (
    <SafeAreaView style={styles.safeArea}>
      <ScrollView contentContainerStyle={styles.container}>
        <View style={styles.header}>
          <Text style={styles.headerText}>Your Profile</Text>
          <Text style={styles.descriptionText}>Manage your profile and settings here.</Text>
        </View>
        <View style={styles.content}>
          <Text style={styles.sectionTitle}>Profile Information</Text>
          <Text style={styles.infoLabel}>Name: John Doe</Text>
          <Text style={styles.infoLabel}>Email: john.doe@example.com</Text>
          <Text style={styles.infoLabel}>Room Number: 12B</Text>
        </View>
        <View style={styles.content}>
          <Text style={styles.sectionTitle}>Settings</Text>
          <TouchableOpacity style={styles.optionButton}>
            <Text style={styles.optionText}>Edit Profile</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.optionButton}>
            <Text style={styles.optionText}>Change Password</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.optionButton}>
            <Text style={styles.optionText}>Notification Settings</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: 'white',
  },
  container: {
    padding: 16,
  },
  header: {
    marginBottom: 24,
  },
  headerText: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 8,
  },
  descriptionText: {
    fontSize: 16,
    color: 'gray',
    textAlign: 'center',
  },
  content: {
    padding: 16,
    marginBottom: 16,
    backgroundColor: 'white',
    borderRadius: 8,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  infoLabel: {
    fontSize: 16,
    marginBottom: 4,
  },
  optionButton: {
    backgroundColor: 'black',
    padding: 12,
    borderRadius: 8,
    marginTop: 8,
    alignItems: 'center',
  },
  optionText: {
    color: 'white',
    fontSize: 16,
  },
});
