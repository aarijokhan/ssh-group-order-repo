import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from '../(tabs)/index'; 
import GroupOrderScreen from '../(tabs)/group-order';
import ExploreScreen from '../(tabs)/explore'; 
import ProfileScreen from '../(tabs)/profile'; 
import MarketplaceScreen from '../(tabs)/marketplace';


const Stack = createStackNavigator();

export default function AppNavigator() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="group-order" component={GroupOrderScreen} />
        <Stack.Screen name="explore" component={ExploreScreen} />
        <Stack.Screen name="profile" component={ProfileScreen} />
        <Stack.Screen name="marketplace" component={MarketplaceScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
