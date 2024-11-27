import React from 'react';
import { View, Text, StyleSheet, SafeAreaView, ScrollView, Image } from 'react-native';

export default function HomeScreen() {
  return (
    <SafeAreaView style={styles.safeArea}>
      <ScrollView contentContainerStyle={styles.container}>
        {/* Header Section */}
        <View style={styles.header}>
          <Image
            source={require('/Users/Fizan/Downloads/SshFrontEnd/SSH/assets/images/IMG_6604.jpg')}
            style={styles.logo}
          />
          <Text style={styles.headerText}>Welcome to SSH!</Text>
        </View>
      </ScrollView> 
    </SafeAreaView> 
  );
}
const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#ffffff',
  },
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
  },
  headerText: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#1d3d47',
  },
  logo: { 
    width: 50,
    height: 50,
    marginRight: 12,
  },
  header: { 
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 24,
  }
}
);
