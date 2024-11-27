import React from 'react';
import { View, Text, StyleSheet, SafeAreaView, ScrollView } from 'react-native';

export default function ProfileScreen() {
    return (
        <SafeAreaView style={styles.safeArea}> 
        <ScrollView contentContainerStyle={styles.container}>
        <View style={styles.container} >
            <Text style={styles.headerText}>Profile</Text>
            <Text style={styles.descriptionText}>This is your profile page. You can view and edit your profile information here.</Text>
        </View>
        </ScrollView>
        </SafeAreaView>
    )
}

const styles = StyleSheet.create({
    safeArea: {
      flex: 1,
      backgroundColor: '#ffffff',
    },
    container: {
      alignItems: 'center',
      padding: 16,
    },
    headerText: {
      fontSize: 20, 
      fontWeight: 'bold',
      color: '#1d3d47',
      flex: 1,
      textAlign: 'center',
    },
    descriptionText: {
      fontSize: 16,
      color: '#666666',
      textAlign: 'center',
    },
}
);