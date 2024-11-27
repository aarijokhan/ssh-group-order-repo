import React from 'react';
import { View, Text, StyleSheet, SafeAreaView, ScrollView, Image, TouchableOpacity } from 'react-native';
import { NavigationProp, useNavigation } from '@react-navigation/native';

type RootStackParamList = {
  'group-order': undefined;
  'explore' : undefined;
}


export default function HomeScreen() {
const navigation = useNavigation<NavigationProp<RootStackParamList>>();

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

  {/* Group order Section */}
  <View style={styles.featureSection}>
  <Text style={styles.featureTitle}>Group Order</Text>
  <Text style={styles.featureDescription}>
    Simplify your grocery shopping with flatmates. Create or join a group, share carts, and split costs effortlessly.
  </Text>
  <TouchableOpacity
    style={styles.actionButton}
    onPress={() => navigation.navigate('group-order')}
  >
    <Text style={styles.actionButtonText}>Start a Group Order</Text>
  </TouchableOpacity>
  </View>

  {/* Explore section*/}
  <View style={styles.featureSection}>
          <Text style={styles.featureTitle}>Explore SSH Features</Text>
          <Text style={styles.featureDescription}>
            Discover SSH's smart solutions tailored for student life. Learn more about how we make living in student accommodations smarter and more efficient.
          </Text>
          <TouchableOpacity
            style={styles.actionButton}
            onPress={() => navigation.navigate('explore')}
          >
            <Text style={styles.actionButtonText}>Explore More</Text>
          </TouchableOpacity>
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
    alignItems: 'center',
    padding: 16,
  },
  headerText: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#1d3d47',
  },
  logo: { 
    width: 100,
    height: 100,
    marginRight: 8,
  },
  header: { 
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 24,
  },
  featureSection: {
    backgroundColor: '#ffffff',
    borderRadius: 12,
    padding: 16,
    marginBottom: 16,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 8,
},
  featureTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 8,
    color: '#333333',
  },
  featureDescription: {
    fontSize: 14,
    color: '#666666',
    marginBottom: 16,
  },
  actionButton: {
    backgroundColor: '#1d3d47',
    borderRadius: 8,
    paddingVertical: 12,
    alignItems: 'center',
  },
  actionButtonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: 'bold',
  },
}
);
